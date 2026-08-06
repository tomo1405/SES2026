import os
import random
import pytest
from src_0674 import task_func

def test_task_func():
    directory = "/tmp/test_directory"
    n_files = 5
    expected_output = n_files

    # Mock the os.path.exists function to make sure the directory doesn't exist before calling task_func
    with patch("os.path.exists", return_value=False):
        actual_output = task_func(directory, n_files)

    assert actual_output == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files

def test_task_func_with_existing_directory():
    directory = "/tmp/test_directory"
    n_files = 5

    # Mock the os.path.exists function to make sure the directory already exists before calling task_func
    with patch("os.path.exists", return_value=True):
        actual_output = task_func(directory, n_files)

    assert actual_output == n_files
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files