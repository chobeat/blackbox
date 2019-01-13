import os
import uuid
from io import BytesIO

from PIL.Image import Image
from flask import (
    flash, redirect, render_template, request, url_for
)
from report_generator import generate_report

from app_creator import app
from face_detector import FaceDetector
from models import Images
from flask import current_app
import collections
from report_generator import render_suggestion
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')


def save_image_in_filesystem(image, filename):
    path = os.path.join(current_app.static_folder, "face_images",filename)
    Image.save(image, open(path, "wb"), "jpeg")


def _save_image(image):
    existing_uuid = Images.insert_if_not_exists(image)
    image_id = existing_uuid or uuid.uuid1()
    filename = Images.generate_filename(image_id)
    url = url_for('static',face_images="face_images",filename=filename)
    save_image_in_filesystem(image, filename)
    return (url, image_id)


def _save_images(analysis_result):
    try:
        return map(_save_image,analysis_result)
    except ValueError:
        return []


def _analysis(file):
    face_images = FaceDetector(file).get_faces_with_features()
    faces=[generate_report(url,image_id) for url,image_id in _save_images(face_images)]


    return render_template("analysis.html", faces=faces, render_suggestion=render_suggestion)


@app.route('/analysis', methods=['POST'])
def analysis():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        bytes_obj = BytesIO()

        file.save(bytes_obj)
        return _analysis(bytes_obj)
    else:
        flash("File not allowed")
        return redirect(request.url)


@app.route('/list', methods=['GET'])
def list():
    with app.app_context():
        images = Images.query.all()

    return str(len(images))
