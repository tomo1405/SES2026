import pytest
from src_1028 import task_func

def test_task_func():
    # Test with a valid URL
    url = "https://www.example.com?q=1234567890"
    assert task_func(url) == "1234567890"

    # Test with a URL that contains a query string but no "q" parameter
    url = "https://www.example.com?a=1234567890"
    assert task_func(url) is None

    # Test with a URL that contains a query string with an invalid hexadecimal value
    url = "https://www.example.com?q=1234567890g"
    assert task_func(url) is None

    # Test with a URL that contains a query string with a valid hexadecimal value but an invalid encoding
    url = "https://www.example.com?q=1234567890"
    assert task_func(url) == "1234567890"

    # Test with a URL that contains a query string with a valid hexadecimal value and a valid encoding
    url = "https://www.example.com?q=1234567890"
    assert task_func(url) == "1234567890"