import pytest
from src_0424 import task_func
import numpy as np
import cv2
import os

# Mocking cv2.imread to avoid reading actual files
class MockCv2Imread:
    def __init__(self, image_data):
        self.image_data = image_data

    def __call__(self, *args, **kwargs):
        return self.image_data

def test_task_func_valid_image_and_threshold(monkeypatch):
    # Mocking image data
    mock_image_data = np.array([[100, 150], [200, 250]], dtype=np.uint8)
    monkeypatch.setattr(cv2, 'imread', MockCv2Imread(mock_image_data))

    # Define test parameters
    image_path = 'test_image.jpg'
    threshold = 128

    # Call the function
    original_img, binary_img = task_func(image_path, threshold)

    # Expected results
    expected_original_img = mock_image_data
    expected_binary_img = np.array([[0, 255], [255, 255]], dtype=np.uint8)

    # Assertions
    assert np.array_equal(original_img, expected_original_img)
    assert np.array_equal(binary_img, expected_binary_img)

def test_task_func_invalid_threshold():
    with pytest.raises(ValueError, match="Threshold must be an integer between 0 and 255."):
        task_func(threshold=-10)

def test_task_func_non_existent_image():
    with pytest.raises(FileNotFoundError, match="No image found at non_existent.jpg"):
        task_func(image_path='non_existent.jpg')