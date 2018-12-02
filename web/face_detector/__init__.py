import face_recognition

from PIL import Image, ImageDraw
class FaceDetector(object):
    def __init__(self, image_file):
        self.img=face_recognition.load_image_file(image_file)

    def get_face_images(self):
        face_locations = face_recognition.face_locations(self.img)
        faces = []
        for face_location in face_locations:

            # Print the location of each face in this image
            top, right, bottom, left = face_location
            # You can access the actual face itself like this:
            face_image = self.img[top:bottom, left:right]
            faces.append(face_image)

        return faces

    def get_faces_with_features(self):
        enriched_faces = []
        for i,face in enumerate(self.get_face_images()):
            face_landmarks_list = face_recognition.face_landmarks(face)
            pil_face = Image.fromarray(face)
            d = ImageDraw.Draw(pil_face)

            for face_landmarks in face_landmarks_list:
                # Let's trace out each facial feature in the image with a line!
                for facial_feature in face_landmarks.keys():
                    d.line(face_landmarks[facial_feature], width=1)

            enriched_faces.append(d)
        return enriched_faces