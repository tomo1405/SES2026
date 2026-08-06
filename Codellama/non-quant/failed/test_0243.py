import pytest
from src_0243 import task_func

def test_task_func_valid_input():
    image_path = 'path/to/image.jpg'
    kernel_size = 5
    blurred_image, ax1, ax2 = task_func(image_path, kernel_size)
    assert isinstance(blurred_image, np.ndarray)
    assert isinstance(ax1, plt.Axes)
    assert isinstance(ax2, plt.Axes)

def test_task_func_invalid_input():
    image_path = 'path/to/image.jpg'
    kernel_size = 0
    with pytest.raises(ValueError):
        task_func(image_path, kernel_size)

def test_task_func_invalid_image_path():
    image_path = 'path/to/invalid/image.jpg'
    kernel_size = 5
    with pytest.raises(FileNotFoundError):
        task_func(image_path, kernel_size)