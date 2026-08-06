python
import requests
from PIL import Image
import io
import pytest

def task_func(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
        return image
    except Exception as e:
        raise ValueError(f"Failed to retrieve image from {url}: {e}") from e

def test_task_func():
    # Test valid URL
    url = "https://www.example.com/image.jpg"
    image = task_func(url)
    assert isinstance(image, Image.Image)

    # Test invalid URL
    url = "https://www.example.com/invalid.jpg"
    with pytest.raises(ValueError):
        task_func(url)