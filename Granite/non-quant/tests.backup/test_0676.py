import os
import random
import pytest
from src_0676 import task_func

def test_task_func():
    directory = "/tmp/test_directory"
    n_files = 5
    expected_output = "/tmp/test_directory"

    # Test with valid input
    result = task_func(directory, n_files)
    assert result == expected_output

    # Test with invalid input (directory already exists)
    os.makedirs(directory)
    with pytest.raises(OSError):
        task_func(directory, n_files)

    # Test with invalid input (n_files is not an integer)
    with pytest.raises(TypeError):
        task_func(directory, "five")

    # Clean up
    os.system("rm -rf /tmp/test_directory")