import pytest
from src_1011 import task_func

def test_task_func():
    url = "https://example.com/image.jpg"
    try:
        image = task_func(url)
        assert image.width > 0 and image.height > 0
    except ValueError as e:
        assert str(e).startswith("Failed to retrieve image from")