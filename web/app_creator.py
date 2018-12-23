from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
STATIC_FOLDER = "static"
def create_app(test_config=None):
    app = Flask(__name__, static_folder = STATIC_FOLDER)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blackbox.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/test.db'


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ensure the instance folder exists
    try:
        os.makedirs(app.static_folder)
    except OSError:
        pass


    return app


app = create_app()
