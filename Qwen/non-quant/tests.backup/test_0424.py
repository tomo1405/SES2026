import pytest
from src_0424 import task_func
import numpy as np
import cv2
import os

def test_task_func_invalid_threshold():
    with pytest.raises(ValueError):
        task_func(threshold=256)

    with pytest.raises(ValueError):
        task_func(threshold=-1)

    with pytest.raises(ValueError):
        task_func(threshold=128.5)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent.jpg')

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    image_path = str(tmpdir.join('test_image.png'))
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=127)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.zeros((100, 100), dtype=np.uint8))

    # Test with a different threshold
    binary_img_high_threshold = task_func(image_path=image_path, threshold=1)[1]
    assert np.array_equal(binary_img_high_threshold, np.ones((100, 100), dtype=np.uint8))