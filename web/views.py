import os
from werkzeug.utils import secure_filename
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app import *
from flask import current_app
import logging
from face_detector import FaceDetector

demo_bp = Blueprint('demo', __name__, url_prefix='/demo')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_DIRECTORY ="uploaded_images"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@demo_bp.route('/upload', methods=['GET'])
def upload():

    return render_template('upload.html')


def _analysis(file):
    return FaceDetector(file.read()).get_faces_with_features()

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
            path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            file.save(path)
        else:
            flash("File not allowed")
            return redirect(request.url)

        return "\n".join(_analysis(file))