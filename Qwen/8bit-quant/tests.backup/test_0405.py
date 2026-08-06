import pytest
from src_0405 import task_func
import cv2
import numpy as np
import os
from unittest.mock import patch

# Mocking cv2.imread to return a dummy image
dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)

@patch('cv2.imread', return_value=dummy_image)
def test_task_func_valid_image(mock_imread):
    img_path = 'valid_image.jpg'
    img, contours = task_func(img_path)
    assert isinstance(img, np.ndarray)
    assert len(img.shape) == 3
    assert img.shape[2] == 3
    assert isinstance(contours, list)

def test_task_func_file_not_found():
    img_path = 'non_existent_image.jpg'
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(img_path)
    assert str(excinfo.value) == f"No file found at {img_path}"

@patch('cv2.imread', return_value=None)
def test_task_func_invalid_image(mock_imread):
    img_path = 'invalid_image.jpg'
    with pytest.raises(cv2.error) as excinfo:
        task_func(img_path)
    assert "error" in str(excinfo.value)