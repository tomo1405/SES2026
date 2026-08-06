python
import pytest
from src_0424 import task_func

def test_task_func():
    # Test with valid input
    img, binary_img = task_func('image.jpg', 128)
    assert img.shape == (256, 256)
    assert binary_img.shape == (256, 256)
    assert binary_img.dtype == 'uint8'
    assert (binary_img == 255).sum() > 0

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func('image.jpg', '128')

    with pytest.raises(FileNotFoundError):
        task_func('invalid_image.jpg', 128)