import pytest
from src_1011 import task_func

def test_task_func():
    with pytest.raises(ValueError) as exc_info:
        task_func("http://invalid-url")
    assert "Failed to retrieve image from http://invalid-url" in str(exc_info.value)

def test_task_func_valid_url():
    image = task_func("https://example.com/image.jpg")
    assert image.size == (800, 600)