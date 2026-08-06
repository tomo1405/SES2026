import pytest
from src_0405 import task_func

def test_task_func_valid_input():
    img_path = "path/to/image.jpg"
    img, contours = task_func(img_path)
    assert isinstance(img, np.ndarray)
    assert isinstance(contours, list)
    assert len(contours) > 0

def test_task_func_invalid_input():
    img_path = "path/to/invalid/image.jpg"
    with pytest.raises(FileNotFoundError):
        task_func(img_path)