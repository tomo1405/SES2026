import numpy as np
import cv2
import os
import pytest
from src_0424 import task_func

def test_task_func_with_valid_input():
    image_path = 'image.jpg'
    threshold = 128
    img, binary_img = task_func(image_path, threshold)
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert img.dtype == np.uint8
    assert binary_img.dtype == np.uint8
    assert img.shape == binary_img.shape

def test_task_func_with_invalid_threshold():
    image_path = 'image.jpg'
    threshold = 256
    with pytest.raises(ValueError) as excinfo:
        task_func(image_path, threshold)
    assert "Threshold must be an integer between 0 and 255." in str(excinfo.value)

def test_task_func_with_nonexistent_image_path():
    image_path = 'nonexistent_image.jpg'
    threshold = 128
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(image_path, threshold)
    assert f"No image found at {image_path}" in str(excinfo.value)