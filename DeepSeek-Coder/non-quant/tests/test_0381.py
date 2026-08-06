import pytest
from src_0381 import task_func
import os
import shutil
import re

@pytest.fixture
def setup_and_teardown():
    # Create a temporary directory for testing
    test_dir = "test_directory"
    os.makedirs(test_dir)
    yield test_dir
    # Clean up: remove the test directory and its contents
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(test_dir)

def test_task_func(setup_and_teardown):
    test_dir = setup_and_teardown
    # Create some test files and directories
    test_files = ["file1.txt", "file2.txt", "file3.jpg"]
    for file in test_files:
        with open(os.path.join(test_dir, file), "w") as f:
            f.write("test")
    
    task_func(test_dir)
    
    # Check if files are moved to the correct directories
    expected_dirs = {"txt": "file1.txt", "txt": "file2.txt", "jpg": "file3.jpg"}
    for ext, filename in expected_dirs.items():
        assert os.path.exists(os.path.join(test_dir, ext, filename))

    # Clean up: remove the test files and directories
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(test_dir)