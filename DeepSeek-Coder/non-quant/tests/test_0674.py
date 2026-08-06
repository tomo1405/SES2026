import pytest
from src_0674 import task_func
import os
import random

def test_task_func():
    # Test with a valid directory and number of files
    directory = "test_directory"
    n_files = 3
    result = task_func(directory, n_files)
    assert result == n_files
    assert len(os.listdir(directory)) == n_files

    # Clean up: remove the test directory and its contents
    for filename in os.listdir(directory):
        os.remove(os.path.join(directory, filename))
    os.rmdir(directory)

    # Test with an invalid directory
    invalid_directory = "invalid_directory"
    with pytest.raises(FileNotFoundError):
        task_func(invalid_directory, n_files)