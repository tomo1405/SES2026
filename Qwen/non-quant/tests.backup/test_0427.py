import pytest
from src_0427 import task_func
import numpy as np
import cv2
import os

def test_task_func_invalid_threshold():
    with pytest.raises(ValueError):
        task_func(threshold=-1)
    with pytest.raises(ValueError):
        task_func(threshold=256)
    with pytest.raises(ValueError):
        task_func(threshold=128.5)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent.jpg')

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    img_array = np.ones((10, 10), dtype=np.uint8) * 128
    temp_image_path = str(tmpdir / 'temp_image.jpg')
    cv2.imwrite(temp_image_path, img_array)

    # Call the function
    original_img, binary_img = task_func(image_path=temp_image_path, threshold=128)

    # Check if the original image is correct
    assert np.array_equal(original_img, img_array)

    # Check if the binary image is correct
    expected_binary_img = np.ones((10, 10), dtype=np.uint8) * 255
    assert np.array_equal(binary_img, expected_binary_img)

    # Check if the binary image file was created
    assert os.path.exists('binary_image.jpg')

    # Clean up the binary image file
    os.remove('binary_image.jpg')