import pytest
from src_0369 import task_func
import os
import tempfile

def test_task_func_with_files():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some files in the source directory
        file_names = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in file_names:
            with open(os.path.join(src_dir, file_name), 'w') as f:
                f.write('Sample content')

        # Call the function
        moved_file = task_func(src_dir, dest_dir)

        # Check if the file was moved to the destination directory
        assert moved_file in file_names
        assert os.path.exists(os.path.join(dest_dir, moved_file))
        assert not os.path.exists(os.path.join(src_dir, moved_file))

def test_task_func_no_files():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Call the function and expect a FileNotFoundError
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(src_dir, dest_dir)
        assert "No files found in" in str(excinfo.value)

def test_task_func_with_empty_source_directory():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Call the function and expect a FileNotFoundError
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(src_dir, dest_dir)
        assert "No files found in" in str(excinfo.value)

def test_task_func_with_single_file():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create a single file in the source directory
        file_name = 'single_file.txt'
        with open(os.path.join(src_dir, file_name), 'w') as f:
            f.write('Sample content')

        # Call the function
        moved_file = task_func(src_dir, dest_dir)

        # Check if the file was moved to the destination directory
        assert moved_file == file_name
        assert os.path.exists(os.path.join(dest_dir, moved_file))
        assert not os.path.exists(os.path.join(src_dir, moved_file))

def test_task_func_with_seed():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some files in the source directory
        file_names = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in file_names:
            with open(os.path.join(src_dir, file_name), 'w') as f:
                f.write('Sample content')

        # Call the function with a specific seed
        moved_file = task_func(src_dir, dest_dir, seed=42)

        # Check if the file was moved to the destination directory
        assert moved_file in file_names
        assert os.path.exists(os.path.join(dest_dir, moved_file))
        assert not os.path.exists(os.path.join(src_dir, moved_file))