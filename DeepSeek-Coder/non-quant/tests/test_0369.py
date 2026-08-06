import pytest
from src_0369 import task_func
import os
import shutil
import random

# Mocking the random.seed function to control the random behavior
def mock_seed(seed):
    random.seed(seed)

# Mocking the os.listdir function to return a predefined list of files
def mock_listdir(dir):
    return ["file1.txt", "file2.txt", "file3.txt"]

# Mocking the os.path.join function
def mock_join(dir, file):
    return os.path.join(dir, file)

# Mocking the shutil.move function
def mock_move(src, dest):
    return shutil.move(src, dest)

# Test cases
def test_task_func():
    # Setting up the mocks
    original_listdir = os.listdir
    original_seed = random.seed
    original_move = shutil.move

    try:
        os.listdir = mock_listdir
        random.seed = mock_seed
        shutil.move = mock_move
        os.path.join = mock_join

        # Test case 1: Normal operation
        result = task_func("src_dir", "dest_dir")
        assert result == "file1.txt"

        # Test case 2: No files in the source directory
        os.listdir = lambda dir: []
        with pytest.raises(FileNotFoundError):
            task_func("src_dir", "dest_dir")

    finally:
        os.listdir = original_listdir
        random.seed = original_seed
        shutil.move = original_move