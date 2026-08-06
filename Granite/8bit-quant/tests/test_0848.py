import re
import os
import string
import random
from src_0848 import task_func
def test_task_func():
    input_string = "Hello, world!\nThis is a test."
    file_paths = task_func(input_string)
    for file_path in file_paths:
        assert os.path.isfile(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
            assert content in input_string
    assert len(file_paths) == 2
def test_task_func_with_directory():
    input_string = "Hello, world!\nThis is a test."
    directory = './test_files'
    file_paths = task_func(input_string, directory)
    for file_path in file_paths:
        assert os.path.isfile(file_path)
        assert file_path.startswith(directory)
        with open(file_path, 'r') as file:
            content = file.read()
            assert content in input_string
    assert len(file_paths) == 2