import cv2
import numpy as np
import os
import pytest

from src_0405 import task_func

def test_task_func():
    img_path = "path/to/image.jpg"
    img, contours = task_func(img_path)
    
    assert isinstance(img, np.ndarray), "img should be a numpy array"
    assert isinstance(contours, list), "contours should be a list"
    
    for contour in contours:
        assert isinstance(contour, np.ndarray), "contour should be a numpy array"
    
    with pytest.raises(FileNotFoundError):
        task_func("invalid/path/to/image.jpg")