python
import pytest
from src_0427 import task_func

def test_task_func():
    # Test with valid input
    img, binary_img = task_func(image_path='image.jpg', threshold=128)
    assert img.shape == (200, 300)
    assert binary_img.shape == (200, 300)
    assert binary_img.dtype == 'uint8'
    assert (binary_img == 0).sum() + (binary_img == 255).sum() == 62500

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(image_path='image.jpg', threshold='128')

    with pytest.raises(FileNotFoundError):
        task_func(image_path='invalid_image.jpg', threshold=128)