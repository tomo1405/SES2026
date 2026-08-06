import pytest
from src_1051 import task_func

def test_task_func():
    input_string = "Hello\nWorld\n"
    expected_file_paths = [
        "./hashed_files/1234567890.txt",
        "./hashed_files/abcdef0123.txt"
    ]

    file_paths = task_func(input_string)

    assert file_paths == expected_file_paths