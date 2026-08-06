import pytest
from src_0908 import task_func

def test_task_func_valid_pattern():
    pattern = r"^[a-zA-Z0-9_-]+\.txt$"
    replacement = r"new_file.txt"
    directory = "test_dir"
    assert task_func(pattern, replacement, directory) == True

def test_task_func_invalid_pattern():
    pattern = r"^[a-zA-Z0-9_-]+\.txt$"
    replacement = r"new_file.txt"
    directory = "test_dir"
    assert task_func(pattern, replacement, directory) == False

def test_task_func_invalid_replacement():
    pattern = r"^[a-zA-Z0-9_-]+\.txt$"
    replacement = r"new_file.txt"
    directory = "test_dir"
    assert task_func(pattern, replacement, directory) == False

def test_task_func_invalid_directory():
    pattern = r"^[a-zA-Z0-9_-]+\.txt$"
    replacement = r"new_file.txt"
    directory = "test_dir"
    assert task_func(pattern, replacement, directory) == False