import pytest
from src_0404 import task_func

def test_task_func_valid_input():
    img_path = "path/to/image.jpg"
    blur_radius = 5
    img, grey_img = task_func(img_path, blur_radius)
    assert isinstance(img, np.ndarray)
    assert isinstance(grey_img, np.ndarray)
    assert img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)

def test_task_func_invalid_input():
    img_path = "path/to/image.jpg"
    blur_radius = 5
    with pytest.raises(FileNotFoundError):
        task_func(img_path, blur_radius)