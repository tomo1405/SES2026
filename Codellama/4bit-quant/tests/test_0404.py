import pytest
from src_0404 import task_func

def test_task_func():
    img_path = "path/to/image.jpg"
    blur_radius = 5

    img, grey_img = task_func(img_path, blur_radius)

    assert img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)

def test_task_func_invalid_path():
    img_path = "path/to/invalid/image.jpg"
    blur_radius = 5

    with pytest.raises(FileNotFoundError):
        task_func(img_path, blur_radius)