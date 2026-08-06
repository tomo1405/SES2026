import pytest
from src_0908 import task_func

def test_task_func():
    pattern = r"^[a-zA-Z]+"
    replacement = r"new_"
    directory = "path/to/directory"
    result = task_func(pattern, replacement, directory)
    assert result == True

def test_task_func_invalid_pattern():
    pattern = r"^[a-zA-Z]+"
    replacement = r"new_"
    directory = "path/to/directory"
    result = task_func(pattern, replacement, directory)
    assert result == False

def test_task_func_invalid_replacement():
    pattern = r"^[a-zA-Z]+"
    replacement = r"new_"
    directory = "path/to/directory"
    result = task_func(pattern, replacement, directory)
    assert result == False

def test_task_func_invalid_directory():
    pattern = r"^[a-zA-Z]+"
    replacement = r"new_"
    directory = "path/to/directory"
    result = task_func(pattern, replacement, directory)
    assert result == False