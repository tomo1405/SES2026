import subprocess
import os
import random
from src_0321 import task_func

def test_task_func_with_valid_input():
    directory = "/path/to/directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    random.seed(123)  # Set random seed for reproducibility
    exit_code = task_func(directory, file_list)
    assert exit_code is not None

def test_task_func_with_empty_file_list():
    directory = "/path/to/directory"
    file_list = []
    exit_code = task_func(directory, file_list)
    assert exit_code is None

def test_task_func_with_invalid_directory():
    directory = "/path/to/invalid_directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    random.seed(123)  # Set random seed for reproducibility
    exit_code = task_func(directory, file_list)
    assert exit_code is None

def test_task_func_with_invalid_file_list():
    directory = "/path/to/directory"
    file_list = ["file1.txt", "file2.txt", "file3.txt", "invalid_file.txt"]
    random.seed(123)  # Set random seed for reproducibility
    exit_code = task_func(directory, file_list)
    assert exit_code is None