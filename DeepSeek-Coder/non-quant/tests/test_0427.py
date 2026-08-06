import pytest
from src_0427 import task_func
import os

@pytest.fixture
def setup_teardown():
    # Setup code
    yield
    # Teardown code
    if os.path.exists('binary_image.jpg'):
        os.remove('binary_image.jpg')

def test_task_func_valid_input(setup_teardown):
    img, binary_img = task_func('tests/test_image.jpg', 128)
    assert img.shape == (480, 640)  # Assuming the image is 480x640
    assert binary_img.shape == (480, 640)
    assert np.array_equal(img, np.array(cv2.imread('tests/test_image.jpg', cv2.IMREAD_GRAYSCALE)))
    assert np.array_equal(binary_img, np.where(img >= 128, 255, 0))

def test_invalid_image_path(setup_teardown):
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_image.jpg', 128)

def test_invalid_threshold(setup_teardown):
    with pytest.raises(ValueError):
        task_func('tests/test_image.jpg', 256)