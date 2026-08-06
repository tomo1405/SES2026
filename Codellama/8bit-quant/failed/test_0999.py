import pytest
from src_0999 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com/file.tar.gz"
    assert task_func(url) == True

def test_task_func_invalid_url():
    url = "https://www.example.com/file.tar.gz"
    with pytest.raises(Exception):
        task_func(url)

def test_task_func_invalid_checksum():
    url = "https://www.example.com/file.tar.gz"
    with pytest.raises(Exception):
        task_func(url)

def test_task_func_invalid_file():
    url = "https://www.example.com/file.tar.gz"
    with pytest.raises(Exception):
        task_func(url)