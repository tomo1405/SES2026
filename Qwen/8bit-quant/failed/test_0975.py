import pytest
from src_0975 import task_func
import shutil
import pathlib
import tempfile

def test_task_func_with_valid_directory():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some files in the source directory
        file1 = pathlib.Path(src_dir) / 'file1.txt'
        file2 = pathlib.Path(src_dir) / 'file2.txt'
        file1.touch()
        file2.touch()

        # Call the function
        result = task_func(src_dir, dest_dir)

        # Check the result
        assert result == ('', ['file1.txt', 'file2.txt'])

        # Check if files are copied to the destination directory
        assert (pathlib.Path(dest_dir) / 'file1.txt').exists()
        assert (pathlib.Path(dest_dir) / 'file2.txt').exists()

def test_task_func_with_nonexistent_source_directory():
    with tempfile.TemporaryDirectory() as dest_dir:
        # Call the function with a non-existent source directory
        with pytest.raises(ValueError) as excinfo:
            task_func('non_existent_dir', dest_dir)

        # Check the exception message
        assert str(excinfo.value) == "source_path must be an existing directory."

def test_task_func_with_empty_source_directory():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Call the function with an empty source directory
        result = task_func(src_dir, dest_dir)

        # Check the result
        assert result == ('', [])

        # Check if the destination directory is empty
        assert len(list(pathlib.Path(dest_dir).iterdir())) == 0

def test_task_func_with_nested_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create nested directories and files in the source directory
        subdir = pathlib.Path(src_dir) / 'subdir'
        subdir.mkdir()
        file1 = subdir / 'file1.txt'
        file2 = subdir / 'file2.txt'
        file1.touch()
        file2.touch()

        # Call the function
        result = task_func(src_dir, dest_dir)

        # Check the result
        assert result == ('', ['subdir/file1.txt', 'subdir/file2.txt'])

        # Check if files are copied to the destination directory
        assert (pathlib.Path(dest_dir) / 'subdir' / 'file1.txt').exists()
        assert (pathlib.Path(dest_dir) / 'subdir' / 'file2.txt').exists()