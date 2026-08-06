import pytest
from src_1011 import task_func
import requests
from PIL import Image
import io

def test_task_func_success():
    url = "https://example.com/image.jpg"
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(io.BytesIO(response.content))
    
    result = task_func(url)
    assert result == image

def test_task_func_failure():
    url = "invalid-url"
    with pytest.raises(ValueError):
        task_func(url)