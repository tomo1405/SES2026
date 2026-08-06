import pytest
from src_0243 import task_func

def test_task_func():
    image_path = "path/to/image.jpg"
    kernel_size = 5

    with pytest.raises(ValueError):
        task_func(image_path, -1)

    with pytest.raises(FileNotFoundError):
        task_func("path/to/nonexistent/image.jpg", kernel_size)

    blurred_image, ax1, ax2 = task_func(image_path, kernel_size)

    assert blurred_image.shape == (height, width, 3)
    assert ax1.get_title() == "Original"
    assert ax2.get_title() == "Blurred"