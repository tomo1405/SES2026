import pytest
from src_0196 import task_func

def test_task_func():
    # Test with a valid URL
    url = 'https://www.example.com'
    assert task_func(url) == 0

    # Test with an invalid URL
    url = 'invalid_url'
    assert task_func(url) == 1

    # Test with a valid URL and a custom command
    url = 'https://www.example.com'
    cmd = 'open'
    assert task_func(url, cmd) == 0

    # Test with an invalid URL and a custom command
    url = 'invalid_url'
    cmd = 'open'
    assert task_func(url, cmd) == 1