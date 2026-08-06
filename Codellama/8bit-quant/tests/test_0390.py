import os
import re

import pytest
from src_0390 import task_func


def test_task_func():
    directory = 'test_directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    assert task_func(directory) == interesting_files

def test_task_func_no_interesting_files():
    directory = 'test_directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = []

    assert task_func(directory) == interesting_files

def test_task_func_invalid_directory():
    directory = 'invalid_directory'
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = []

    with pytest.raises(FileNotFoundError):
        task_func(directory)