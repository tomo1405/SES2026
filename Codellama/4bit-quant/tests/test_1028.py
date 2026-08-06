import pytest
from src_1028 import task_func

def test_task_func():
    # Test with a valid URL
    url = "https://www.example.com?q=1234567890"
    assert task_func(url) == "1234567890"

    # Test with a URL that has no query string
    url = "https://www.example.com"
    assert task_func(url) is None

    # Test with a URL that has a query string with an invalid hex string
    url = "https://www.example.com?q=invalid"
    assert task_func(url) is None

    # Test with a URL that has a query string with a valid hex string but invalid encoding
    url = "https://www.example.com?q=1234567890%20"
    assert task_func(url) is None