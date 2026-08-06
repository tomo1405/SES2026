python
import pytest
from src_0424 import task_func

def test_task_func():
    # Test case 1: Valid input
    img, binary_img = task_func('image.jpg', 128)
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert img.shape == (512, 512)
    assert binary_img.shape == (512, 512)
    assert binary_img.dtype == 'uint8'
    assert np.all(binary_img == np.where(img > 128, 255, 0))

    # Test case 2: Invalid threshold
    with pytest.raises(ValueError):
        task_func('image.jpg', 256)

    # Test case 3: Invalid image path
    with pytest.raises(FileNotFoundError):
        task_func('invalid_image.jpg', 128)