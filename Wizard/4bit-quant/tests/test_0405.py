python
import cv2
import numpy as np
import os
import pytest

def task_func(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find contours
    contours, _ = cv2.findContours(gray_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return np.array(img), contours

def test_task_func():
    img_path = "path/to/image.jpg"
    img, contours = task_func(img_path)
    
    assert isinstance(img, np.ndarray)
    assert isinstance(contours, list)
    assert len(contours) > 0
    assert isinstance(contours[0], np.ndarray)