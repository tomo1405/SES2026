import os
import re
import pytest
from src_0908 import task_func

def test_task_func_valid_input():
    pattern = "pattern"
    replacement = "replacement"
    directory = "directory"
    assert task_func(pattern, replacement, directory) == True

def test_task_func_invalid_input():
    pattern = "pattern"
    replacement = "replacement"
    directory = "directory"
    with pytest.raises(Exception):
        task_func(pattern, replacement, directory)

def test_task_func_file_not_found():
    pattern = "pattern"
    replacement = "replacement"
    directory = "directory"
    with pytest.raises(FileNotFoundError):
        task_func(pattern, replacement, directory)