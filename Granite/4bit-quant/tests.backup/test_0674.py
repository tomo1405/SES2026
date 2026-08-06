import os
import random
import pytest

from src_0674 import task_func

def test_task_func():
    directory = "/tmp/test_directory"
    n_files = 5
    expected_output = n_files

    # Test when directory does not exist
    if os.path.exists(directory):
        os.rmdir(directory)
    result = task_func(directory, n_files)
    assert result == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == n_files

    # Test when directory already exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    result = task_func(directory, n_files)
    assert result == expected_output
    assert os.path.exists(directory)
    assert len(os.listdir(directory)) == 2 * n_files

    # Clean up
    os.rmdir(directory)

if __name__ == "__main__":
    pytest.main()