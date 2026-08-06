import pytest
from src_1017 import task_func

def test_task_func():
    # Test with a valid URL
    url = "https://example.com/image.jpg"
    ax = task_func(url)
    assert ax is not None, "The function should return a valid Axes object"

    # Add more tests as needed to cover different scenarios