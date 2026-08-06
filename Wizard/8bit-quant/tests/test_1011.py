python
import pytest
from src_1011 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com/image.jpg"
    image = task_func(url)
    assert isinstance(image, Image.Image)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid.jpg"
    with pytest.raises(ValueError) as e:
        task_func(url)
    assert str(e.value) == f"Failed to retrieve image from {url}: 404 Client Error: Not Found for url: {url}"