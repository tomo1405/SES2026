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
        task_func(threshold=3.14)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent.jpg')

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    image_path = str(tmpdir / 'test_image.jpg')
    img = np.ones((100, 100), dtype=np.uint8) * 128
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=128)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.zeros((100, 100), dtype=np.uint8))

def test_task_func_binary_conversion(tmpdir):
    # Create a temporary image file
    image_path = str(tmpdir / 'test_image.jpg')
    img = np.ones((100, 100), dtype=np.uint8) * 192
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=128)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.ones((100, 100), dtype=np.uint8) * 255)