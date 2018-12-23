from extensions import db


class Images(db.Model):

    uuid = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(80), nullable=False)
    filename = db.Column(db.String(80), nullable=False)

