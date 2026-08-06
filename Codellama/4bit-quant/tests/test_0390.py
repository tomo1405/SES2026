import os
import re

import pytest
from src_0390 import task_func


def test_task_func():
    directory = 'path/to/directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    assert task_func(directory) == interesting_files

def test_task_func_with_invalid_directory():
    directory = 'path/to/invalid/directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    with pytest.raises(ValueError):
        task_func(directory)

def test_task_func_with_no_interesting_files():
    directory = 'path/to/directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = []

    assert task_func(directory) == interesting_files