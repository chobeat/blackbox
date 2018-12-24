import uuid

from imagehash import average_hash

from extensions import db
from flask import current_app


class Images(db.Model):
    uuid = db.Column(db.String(80), primary_key=True)
    hash = db.Column(db.String(80), nullable=False)
    filename = db.Column(db.String(80), nullable=False)

    @staticmethod
    def generate_filename(image_id):
        return str(image_id) + ".jpeg"

    @staticmethod
    def insert_if_not_exists(image):

        hash = str(average_hash(image))
        matching_images = Images.query.filter_by(hash=hash).first()


        if matching_images:
            return matching_images.uuid
        else:
            image_id = str(uuid.uuid1())
            image_model = Images(uuid=image_id, hash=hash,
                                 filename=Images.generate_filename(image_id))
            db.session.add(image_model)
            db.session.commit()
            return image_id
