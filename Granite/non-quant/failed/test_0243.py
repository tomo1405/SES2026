import pytest
from src_0243 import task_func

def test_task_func_valid_input():
    image_path = "path/to/image.jpg"
    kernel_size = 5
    blurred_image, ax1, ax2 = task_func(image_path, kernel_size)
    assert blurred_image is not None
    assert ax1 is not None
    assert ax2 is not None

def test_task_func_invalid_kernel_size():
    image_path = "path/to/image.jpg"
    kernel_size = -1
    with pytest.raises(ValueError) as e:
        task_func(image_path, kernel_size)
    assert "kernel_size must be a positive integer" in str(e.value)

def test_task_func_file_not_found():
    image_path = "path/to/nonexistent_image.jpg"
    kernel_size = 5
    with pytest.raises(FileNotFoundError) as e:
        task_func(image_path, kernel_size)
    assert f"No image found at {image_path}" in str(e.value)