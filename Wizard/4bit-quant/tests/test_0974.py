python
import os
import shutil
import pytest

from src_0974 import task_func

def test_task_func_valid_path():
    path = "/home/user/Documents/example.txt"
    expected_result = [
        ("/", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("/home", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("/home/user", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("/home/user/Documents", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("/home/user/Documents/example.txt", {"total": 1000000000, "used": 500000000, "free": 500000000}),
    ]
    assert task_func(path) == expected_result

def test_task_func_invalid_path():
    path = "/invalid/path"
    with pytest.raises(FileNotFoundError):
        task_func(path)

def test_task_func_empty_path():
    path = ""
    with pytest.raises(ValueError):
        task_func(path)

def test_task_func_invalid_delimiter():
    path = "/home/user/Documents/example.txt"
    delimiter = ":"
    with pytest.raises(ValueError):
        task_func(path, delimiter)