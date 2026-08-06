import pytest
from src_0427 import task_func
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
        task_func(image_path='nonexistent_image.jpg')

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    image_path = str(tmpdir.join('test_image.jpg'))
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=128)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.zeros_like(img))

    # Check if the binary image is saved correctly
    saved_binary_img = cv2.imread('binary_image.jpg', cv2.IMREAD_GRAYSCALE)
    assert np.array_equal(saved_binary_img, binary_img)

def test_task_func_threshold_0(tmpdir):
    image_path = str(tmpdir.join('test_image.jpg'))
    img = np.full((100, 100), 255, dtype=np.uint8)
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=0)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.full_like(img, 255))

def test_task_func_threshold_255(tmpdir):
    image_path = str(tmpdir.join('test_image.jpg'))
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite(image_path, img)

    original_img, binary_img = task_func(image_path=image_path, threshold=255)

    assert np.array_equal(original_img, img)
    assert np.array_equal(binary_img, np.zeros_like(img))