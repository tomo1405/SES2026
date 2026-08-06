import os

import pytest
from src_0369 import task_func


def test_task_func_valid_input():
    src_dir = "path/to/src/dir"
    dest_dir = "path/to/dest/dir"
    seed = 100
    file_name = "test_file.txt"

    # Set up the test environment
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(src_dir, file_name), "w") as f:
        f.write("Test file content")

    # Run the function
    result = task_func(src_dir, dest_dir, seed)

    # Assert the result
    assert result == file_name
    assert os.path.exists(os.path.join(dest_dir, file_name))
    assert not os.path.exists(os.path.join(src_dir, file_name))

def test_task_func_invalid_input():
    src_dir = "path/to/src/dir"
    dest_dir = "path/to/dest/dir"
    seed = 100
    file_name = "test_file.txt"

    # Set up the test environment
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(src_dir, file_name), "w") as f:
        f.write("Test file content")

    # Run the function
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, seed)

    # Assert the result
    assert not os.path.exists(os.path.join(dest_dir, file_name))
    assert not os.path.exists(os.path.join(src_dir, file_name))