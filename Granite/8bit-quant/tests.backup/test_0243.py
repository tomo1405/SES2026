import cv2
import matplotlib.pyplot as plt
import pytest
from src_0243 import task_func

def test_task_func_with_valid_input():
    image_path = "path/to/image.jpg"
    kernel_size = 5
    blurred_image, ax1, ax2 = task_func(image_path, kernel_size)
    assert isinstance(blurred_image, np.ndarray)
    assert isinstance(ax1, plt.Axes)
    assert isinstance(ax2, plt.Axes)

def test_task_func_with_invalid_kernel_size():
    image_path = "path/to/image.jpg"
    kernel_size = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(image_path, kernel_size)
    assert "kernel_size must be a positive integer" in str(excinfo.value)

def test_task_func_with_invalid_image_path():
    image_path = "path/to/invalid_image.jpg"
    kernel_size = 5
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(image_path, kernel_size)
    assert f"No image found at {image_path}" in str(excinfo.value)