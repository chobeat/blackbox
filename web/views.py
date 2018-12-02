import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


demo_bp = Blueprint('demo', __name__, url_prefix='/demo')

@demo_bp.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')