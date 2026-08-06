import pytest
from src_0999 import task_func

def test_task_func():
    url = "https://example.com/file.tar.gz"
    assert task_func(url) == True

def test_task_func_with_invalid_url():
    url = "https://example.com/invalid_file.tar.gz"
    assert task_func(url) == False

def test_task_func_with_corrupted_file():
    url = "https://example.com/corrupted_file.tar.gz"
    assert task_func(url) == False