import pytest
from src_0405 import task_func

def test_task_func():
    img_path = "path/to/image.jpg"
    img, contours = task_func(img_path)
    assert img is not None
    assert contours is not None
    assert len(contours) > 0