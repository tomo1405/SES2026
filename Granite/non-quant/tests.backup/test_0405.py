import cv2
import numpy as np
import os
import pytest
from src_0405 import task_func

def test_task_func():
    img_path = "path/to/image.jpg"
    expected_img = np.array(img)
    expected_contours = contours
    
    img, contours = task_func(img_path)
    
    assert np.array_equal(img, expected_img)
    assert contours == expected_contours