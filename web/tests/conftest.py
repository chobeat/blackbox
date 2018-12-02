import pytest
from pkg_resources import resource_filename
@pytest.fixture
def face_file():
    return resource_filename("resources","face.png")

@pytest.fixture
def faces_file():
    return resource_filename("resources","faces.jpg")