import pytest
from src_0999 import task_func

def test_task_func_success():
    url = "http://example.com/file.tar.gz"
    result = task_func(url)
    assert result is True

def test_task_func_failure():
    url = "http://invalid-url"
    result = task_func(url)
    assert result is False