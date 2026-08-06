python
import pytest
from src_0404 import task_func

def test_task_func():
    img_path = "test_image.jpg"
    img, grey_img = task_func(img_path)

    assert img.shape == (500, 500, 3)
    assert grey_img.shape == (500, 500)