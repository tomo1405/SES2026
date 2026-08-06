import pytest
from src_1011 import task_func

def test_task_func():
    url = "https://www.example.com/image.jpg"
    image = task_func(url)
    assert isinstance(image, Image.Image)
    assert image.mode == "RGB"
    assert image.size == (100, 100)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid.jpg"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_timeout():
    url = "https://www.example.com/timeout.jpg"
    with pytest.raises(requests.Timeout):
        task_func(url)