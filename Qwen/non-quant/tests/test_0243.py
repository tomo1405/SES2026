import pytest
from src_0243 import task_func
import cv2
import numpy as np

def test_task_func_invalid_kernel_size():
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func("path/to/image.jpg", -1)

def test_task_func_non_integer_kernel_size():
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func("path/to/image.jpg", 2.5)

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="No image found at path/to/nonexistent.jpg"):
        task_func("path/to/nonexistent.jpg", 3)

def test_task_func_valid_image_path():
    # Create a temporary image file for testing
    temp_image_path = "temp_test_image.jpg"
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(temp_image_path, image)

    try:
        blurred_image, ax1, ax2 = task_func(temp_image_path, 3)
        assert isinstance(blurred_image, np.ndarray)
        assert blurred_image.shape == image.shape
        assert ax1.get_title() == 'Original'
        assert ax2.get_title() == 'Blurred'
    finally:
        # Clean up the temporary image file
        import os
        os.remove(temp_image_path)