import pytest
from src_0676 import task_func
import os
import random

def test_task_func():
    # Test with a valid directory and number of files
    directory = "test_directory"
    n_files = 5
    result = task_func(directory, n_files)
    
    assert os.path.exists(directory), "Directory should be created"
    assert len(os.listdir(directory)) == n_files, "Number of files should match the specified number"
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as f:
            content = f.read()
            assert int(content) in range(1, 101), "File content should be a random number between 1 and 100"
    
    # Clean up
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))
    os.rmdir(directory)