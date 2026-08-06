import pytest
from src_0769 import task_func
import os
import tempfile

def test_task_func_nonexistent_directory():
    with pytest.raises(ValueError, match="Specified directory does not exist."):
        task_func("/nonexistent/directory")

def test_task_func_no_txt_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_single_txt_file_no_errors():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file.txt"), "w") as file:
            file.write("This is a test file without any errors.")
        result = task_func(temp_dir)
        assert result == {"file.txt": 0}

def test_task_func_single_txt_file_with_errors():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file.txt"), "w") as file:
            file.write("This is a test file with one error and another Error.")
        result = task_func(temp_dir)
        assert result == {"file.txt": 2}

def test_task_func_multiple_txt_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "file1.txt"), "w") as file:
            file.write("This is a test file with one error.")
        with open(os.path.join(temp_dir, "file2.txt"), "w") as file:
            file.write("This is another test file with two Errors.")
        with open(os.path.join(temp_dir, "subdir", "file3.txt"), "w") as file:
            file.write("This file has no errors.")
        os.makedirs(os.path.join(temp_dir, "subdir"))
        result = task_func(temp_dir)
        assert result == {
            "file1.txt": 1,
            "file2.txt": 2,
            "subdir/file3.txt": 0
        }