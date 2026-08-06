import pytest
from src_1051 import task_func

def test_task_func():
    input_string = "Hello\nWorld\n"
    expected_file_paths = [
        "./hashed_files/a948904f2a.txt",
        "./hashed_files/5eb63bbbe0.txt"
    ]
    file_paths = task_func(input_string)
    assert file_paths == expected_file_paths

def test_task_func_empty_input():
    input_string = ""
    expected_file_paths = []
    file_paths = task_func(input_string)
    assert file_paths == expected_file_paths

def test_task_func_invalid_input():
    input_string = "Hello\nWorld\n"
    expected_file_paths = []
    file_paths = task_func(input_string)
    assert file_paths == expected_file_paths