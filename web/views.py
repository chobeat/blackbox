import os
from werkzeug.utils import secure_filename
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import uuid
from flask import current_app
from models import Images
from io import BytesIO
from face_detector import FaceDetector
from PIL.Image import Image
from app_creator import app
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET'])
def upload():

    return render_template('upload.html')

def save_image_in_db(image_id,image_hash,filename):
    pass

def save_image_in_filesystem(image,filename):

    path = os.path.join(demo_bp.static_folder,filename)
    Image.save(image,open(path,"wb"),"jpeg")


def _render_analysis_template(analysis_result):
    urls = []
    for image in analysis_result:
        image_id=uuid.uuid1()
        filename= str(image_id)+".jpeg"
        urls.append(url_for('static', filename=filename))
        save_image_in_filesystem(image, filename)
        image_hash=101
        save_image_in_db(image_id,image_hash,filename)
    return render_template("analysis.html",faces=urls)

def _analysis(file):
    return _render_analysis_template(FaceDetector(file).get_faces_with_features())

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
            filename = secure_filename(file.filename)
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