import pytest
from src_0405 import task_func
import os
import cv2
import numpy as np

@pytest.fixture
def setup():
    # Create a temporary image file for testing
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img_path = "test_image.png"
    cv2.imwrite(img_path, img)
    yield img_path
    os.remove(img_path)

def test_task_func(setup):
    img, contours = task_func(setup)
    assert isinstance(img, np.ndarray), "The returned image should be a numpy array"
    assert len(contours) > 0, "Contours should be detected"