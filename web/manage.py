from app_creator import app
from extensions import db

def register_extensions(app):
    db.init_app(app)
    db.create_all()

if __name__ == "__main__":
    from views import *
    register_extensions(app)
    app.run(host="0.0.0.0",debug=True)