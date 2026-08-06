import pytest
from src_0940 import task_func
import os
import glob
import tempfile
import shutil

def test_task_func():
    # Create a temporary directory and some files with special characters
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with special characters in their names
        file_paths = [
            os.path.join(temp_dir, 'file@name#1.txt'),
            os.path.join(temp_dir, 'another$file%name&2.txt'),
            os.path.join(temp_dir, 'yet-another_file(name).txt')
        ]
        for file_path in file_paths:
            open(file_path, 'a').close()  # Create empty files

        # Call the function
        result = task_func(temp_dir)

        # Check that the files have been renamed correctly
        expected_names = ['filename1.txt', 'anotherfilename2.txt', 'yetanotherfilename.txt']
        assert sorted(result) == sorted(expected_names)

        # Check that the files exist with the new names
        for expected_name in expected_names:
            assert os.path.exists(os.path.join(temp_dir, expected_name))

# Test to ensure the function handles an empty directory
def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []

# Test to ensure the function handles a directory with no files
def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a subdirectory to ensure it doesn't interfere
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        result = task_func(temp_dir)
        assert result == []

# Test to ensure the function handles a directory with only non-renameable files
def test_task_func_non_renameable_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file that is already clean
        file_path = os.path.join(temp_dir, 'cleanfilename.txt')
        open(file_path, 'a').close()
        result = task_func(temp_dir)
        assert result == ['cleanfilename.txt']