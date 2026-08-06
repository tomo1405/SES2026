import re
import os
import string
import random
import pytest

from src_0848 import task_func

def test_task_func():
    input_string = "Hello, world!\nThis is a test line."
    expected_file_paths = [
        './text_files/12345.txt',
        './text_files/67890.txt'
    ]
    actual_file_paths = task_func(input_string)
    assert len(actual_file_paths) == len(expected_file_paths)
    for actual_path, expected_path in zip(actual_file_paths, expected_file_paths):
        assert actual_path == expected_path
        assert os.path.isfile(actual_path)

def test_task_func_with_empty_input():
    input_string = ""
    expected_file_paths = []
    actual_file_paths = task_func(input_string)
    assert actual_file_paths == expected_file_paths

def test_task_func_with_directory_argument():
    input_string = "Another test line."
    expected_directory = '/tmp/text_files'
    expected_file_paths = [
        '/tmp/text_files/54321.txt'
    ]
    actual_file_paths = task_func(input_string, directory=expected_directory)
    assert actual_file_paths == expected_file_paths