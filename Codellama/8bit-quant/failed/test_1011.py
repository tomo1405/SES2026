import pytest
from src_1011 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com/image.jpg"
    image = task_func(url)
    assert isinstance(image, Image.Image)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid.jpg"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_timeout():
    url = "https://www.example.com/timeout.jpg"
    with pytest.raises(requests.Timeout):
        task_func(url)

def test_task_func_connection_error():
    url = "https://www.example.com/connection_error.jpg"
    with pytest.raises(requests.ConnectionError):
        task_func(url)