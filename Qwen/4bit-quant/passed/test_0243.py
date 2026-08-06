import pytest
from src_0243 import task_func
import cv2
import numpy as np
import os

# Mocking cv2.imread to simulate file reading
class MockCv2:
    @staticmethod
    def imread(path):
        if path == "valid_image.jpg":
            return np.ones((100, 100, 3), dtype=np.uint8)
        else:
            return None

@pytest.fixture
def mock_cv2(monkeypatch):
    monkeypatch.setattr(cv2, 'imread', MockCv2.imread)

def test_task_func_valid_image(mock_cv2):
    image_path = "valid_image.jpg"
    kernel_size = 3
    blurred_image, ax1, ax2 = task_func(image_path, kernel_size)
    assert blurred_image.shape == (100, 100, 3)
    assert ax1.get_title() == 'Original'
    assert ax2.get_title() == 'Blurred'

def test_task_func_invalid_kernel_size():
    image_path = "valid_image.jpg"
    kernel_size = -1
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func(image_path, kernel_size)

def test_task_func_non_integer_kernel_size():
    image_path = "valid_image.jpg"
    kernel_size = 3.5
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func(image_path, kernel_size)

def test_task_func_file_not_found(mock_cv2):
    image_path = "non_existent_image.jpg"
    kernel_size = 3
    with pytest.raises(FileNotFoundError, match="No image found at non_existent_image.jpg"):
        task_func(image_path, kernel_size)