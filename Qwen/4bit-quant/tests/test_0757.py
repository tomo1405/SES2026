import pytest
from src_0757 import task_func
from pathlib import Path
import tempfile
import os

def test_task_func_with_valid_directories_and_extensions():
    # Create temporary directories and files
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files with different extensions
        Path(source_dir).joinpath('file1.txt').touch()
        Path(source_dir).joinpath('file2.jpg').touch()
        Path(source_dir).joinpath('file3.pdf').touch()
        Path(source_dir).joinpath('file4.docx').touch()

        # Call the function with specific extensions
        moved_count = task_func(source_dir, target_dir, ['.txt', '.jpg'])

        # Check if the correct number of files were moved
        assert moved_count == 2

        # Check if the files are in the target directory
        assert Path(target_dir).joinpath('file1.txt').exists()
        assert Path(target_dir).joinpath('file2.jpg').exists()

        # Check if the files are not in the source directory anymore
        assert not Path(source_dir).joinpath('file1.txt').exists()
        assert not Path(source_dir).joinpath('file2.jpg').exists()

def test_task_func_with_non_existent_source_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func('non_existent_source', 'valid_target', ['.txt'])
    assert str(excinfo.value) == "source_dir does not exist."

def test_task_func_with_non_existent_target_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func('valid_source', 'non_existent_target', ['.txt'])
    assert str(excinfo.value) == "target_dir does not exist."

def test_task_func_with_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create a file with a non-matching extension
        Path(source_dir).joinpath('file1.png').touch()

        # Call the function with specific extensions
        moved_count = task_func(source_dir, target_dir, ['.txt', '.jpg'])

        # Check if no files were moved
        assert moved_count == 0

        # Check if the file is still in the source directory
        assert Path(source_dir).joinpath('file1.png').exists()

def test_task_func_with_empty_extensions_list():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create a file with any extension
        Path(source_dir).joinpath('file1.txt').touch()

        # Call the function with an empty extensions list
        moved_count = task_func(source_dir, target_dir, [])

        # Check if no files were moved
        assert moved_count == 0

        # Check if the file is still in the source directory
        assert Path(source_dir).joinpath('file1.txt').exists()