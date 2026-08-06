import os
import re
import pytest
from src_0908 import task_func

def test_task_func():
    pattern = r".*\.txt"
    replacement = "new_file.txt"
    directory = "/path/to/directory"
    assert task_func(pattern, replacement, directory) == True

def test_task_func_with_invalid_pattern():
    pattern = r".*\.invalid_extension"
    replacement = "new_file.txt"
    directory = "/path/to/directory"
    assert task_func(pattern, replacement, directory) == False

def test_task_func_with_invalid_directory():
    pattern = r".*\.txt"
    replacement = "new_file.txt"
    directory = "/invalid/path/to/directory"
    with pytest.raises(Exception):
        task_func(pattern, replacement, directory)