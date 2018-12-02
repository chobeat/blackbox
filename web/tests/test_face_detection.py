from  face_detector import FaceDetector

def test_face_locations(face_file):
    faces = FaceDetector(face_file).get_face_images()
    assert len(faces)==1


def test_faces_locations(faces_file):
    faces = FaceDetector(faces_file).get_face_images()
    assert len(faces)==23

def test_face_features(faces_file):
    faces = FaceDetector(faces_file).get_faces_with_features()
    assert len(faces)==23