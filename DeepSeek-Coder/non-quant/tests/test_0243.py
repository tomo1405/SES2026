import pytest
from src_0243 import task_func
import cv2
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    image_path = 'test_image.jpg'
    kernel_size = 5
    return image_path, kernel_size

def test_task_func(setup):
    image_path, kernel_size = setup
    result = task_func(image_path, kernel_size)
    assert result is not None

def test_invalid_kernel_size():
    with pytest.raises(ValueError):
        task_func('test_image.jpg', 'invalid_size')

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_image.jpg', 5)