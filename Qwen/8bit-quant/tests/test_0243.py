import pytest
from src_0243 import task_func
import cv2
import numpy as np

def test_task_func_invalid_kernel_size():
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func("test_image.jpg", -1)

def test_task_func_non_integer_kernel_size():
    with pytest.raises(ValueError, match="kernel_size must be a positive integer"):
        task_func("test_image.jpg", 2.5)

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="No image found at non_existent_image.jpg"):
        task_func("non_existent_image.jpg", 3)

def test_task_func_valid_input(tmpdir):
    # Create a temporary image file for testing
    test_image_path = tmpdir.join("test_image.jpg")
    test_image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(str(test_image_path), test_image)

    blurred_image, ax1, ax2 = task_func(str(test_image_path), 3)

    assert isinstance(blurred_image, np.ndarray)
    assert blurred_image.shape == test_image.shape
    assert ax1.get_title() == 'Original'
    assert ax2.get_title() == 'Blurred'