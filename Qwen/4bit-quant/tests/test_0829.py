import pytest
from src_0829 import task_func
import os
import tempfile
import shutil

def test_task_func():
    # Create a temporary directory and a test file
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "test_file.txt")
        with open(test_file_path, 'w') as f:
            f.write("Sample content")

        # Define the destination directory
        dest_dir = os.path.join(temp_dir, "destination")

        # Call the function
        result = task_func(test_file_path, dest_dir)

        # Check if the file was copied correctly
        assert os.path.exists(os.path.join(dest_dir, "test_file.txt"))

        # Check if the original file is empty
        with open(test_file_path, 'r') as f:
            assert f.read() == ""

        # Check if the returned path is correct
        expected_path = os.path.abspath(os.path.join(dest_dir, "test_file.txt"))
        assert result == expected_path

def test_task_func_nonexistent_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        dest_dir = os.path.join(temp_dir, "destination")
        with pytest.raises(FileNotFoundError):
            task_func("nonexistent_file.txt", dest_dir)

def test_task_func_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "test_file.txt")
        with open(test_file_path, 'w') as f:
            f.write("Sample content")

        # Make the file read-only
        os.chmod(test_file_path, 0o444)

        dest_dir = os.path.join(temp_dir, "destination")
        with pytest.raises(PermissionError):
            task_func(test_file_path, dest_dir)