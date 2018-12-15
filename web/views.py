import os
from werkzeug.utils import secure_filename
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import uuid
from app import *
from flask import current_app
import logging
from io import BytesIO
from face_detector import FaceDetector
from PIL.Image import Image

STATIC_FOLDER = "static"
demo_bp = Blueprint('demo', __name__, url_prefix='/demo',static_url_path="", static_folder=STATIC_FOLDER)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@demo_bp.route('/upload', methods=['GET'])
def upload():

    return render_template('upload.html')

def _render_analysis_template(analysis_result):
    urls = []
    for image in analysis_result:
        filename= str(uuid.uuid1())+".jpeg"
        urls.append(url_for('static', filename=filename))
        path = os.path.join(demo_bp.static_folder,filename)
        Image.save(image,open(path,"wb"),"jpeg")

    return render_template("analysis.html",faces=urls)

def _analysis(file):
    return _render_analysis_template(FaceDetector(file).get_faces_with_features())

@demo_bp.route('/analysis', methods=['POST'])
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

