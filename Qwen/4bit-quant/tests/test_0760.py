import pytest
from src_0760 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary source directory and populate it with files
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some files in the source directory
        file1 = os.path.join(src_dir, 'file1.txt')
        file2 = os.path.join(src_dir, 'file2.txt')
        file3 = os.path.join(src_dir, 'file3.log')
        with open(file1, 'w') as f:
            f.write('content of file1')
        with open(file2, 'w') as f:
            f.write('content of file2')
        with open(file3, 'w') as f:
            f.write('content of file3')

        # Define the file pattern to match .txt files
        file_pattern = '*.txt'

        # Call the function
        moved_files = task_func(src_dir, dest_dir, file_pattern)

        # Check that the correct files were moved
        assert moved_files == ['file1.txt', 'file2.txt']
        assert not os.path.exists(file1)
        assert not os.path.exists(file2)
        assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))

        # Check that the .log file was not moved
        assert os.path.exists(file3)
        assert not os.path.exists(os.path.join(dest_dir, 'file3.log'))

def test_task_func_no_matching_files():
    # Create a temporary source directory without any matching files
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Define the file pattern to match .txt files
        file_pattern = '*.txt'

        # Call the function
        moved_files = task_func(src_dir, dest_dir, file_pattern)

        # Check that no files were moved
        assert moved_files == []
        assert not os.listdir(dest_dir)

def test_task_func_empty_source_directory():
    # Create a temporary empty source directory
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Define the file pattern to match .txt files
        file_pattern = '*.txt'

        # Call the function
        moved_files = task_func(src_dir, dest_dir, file_pattern)

        # Check that no files were moved
        assert moved_files == []
        assert not os.listdir(dest_dir)