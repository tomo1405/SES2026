import pytest
from src_0797 import task_func

def test_task_func():
    directory = 'path/to/directory'
    expected_output = ['path/to/directory/file1.txt', 'path/to/directory/file2.txt']
    assert task_func(directory) == expected_output

def test_task_func_with_invalid_directory():
    directory = 'path/to/invalid/directory'
    expected_output = []
    assert task_func(directory) == expected_output

def test_task_func_with_invalid_bracket_pattern():
    directory = 'path/to/directory'
    expected_output = []
    assert task_func(directory) == expected_output