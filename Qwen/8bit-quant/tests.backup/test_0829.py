import pytest
from src_0829 import task_func
import os
import tempfile
import shutil

def test_task_func():
    # Create a temporary directory and a test file
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "testfile.txt")
        with open(test_file_path, 'w') as test_file:
            test_file.write("Hello, world!")

        # Define the destination directory
        dest_dir = os.path.join(temp_dir, "dest")

        # Call the task_func
        result = task_func(test_file_path, dest_dir)

        # Check if the file was copied to the destination directory
        assert os.path.exists(result)
        assert os.path.isfile(result)

        # Check if the original file content is erased
        with open(test_file_path, 'r') as original_file:
            assert original_file.read() == ""

        # Clean up
        shutil.rmtree(temp_dir)