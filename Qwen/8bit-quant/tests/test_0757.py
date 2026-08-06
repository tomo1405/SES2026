import pytest
from src_0757 import task_func
from pathlib import Path
import shutil
import tempfile

def test_task_func_valid_dirs_and_extensions():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        Path(source_dir, 'file1.txt').touch()
        Path(source_dir, 'file2.docx').touch()
        Path(source_dir, 'file3.pdf').touch()

        # Call the function
        count = task_func(source_dir, target_dir, ['.txt', '.docx'])

        # Check that the correct number of files were moved
        assert count == 2

        # Check that the files are in the target directory
        assert Path(target_dir, 'file1.txt').exists()
        assert Path(target_dir, 'file2.docx').exists()
        assert not Path(target_dir, 'file3.pdf').exists()

def test_task_func_nonexistent_source_dir():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(ValueError) as excinfo:
            task_func('nonexistent_source_dir', target_dir, ['.txt'])
        assert "source_dir does not exist." in str(excinfo.value)

def test_task_func_nonexistent_target_dir():
    with tempfile.TemporaryDirectory() as source_dir:
        with pytest.raises(ValueError) as excinfo:
            task_func(source_dir, 'nonexistent_target_dir', ['.txt'])
        assert "target_dir does not exist." in str(excinfo.value)

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        Path(source_dir, 'file1.txt').touch()
        Path(source_dir, 'file2.docx').touch()

        # Call the function
        count = task_func(source_dir, target_dir, ['.pdf'])

        # Check that no files were moved
        assert count == 0

        # Check that no files are in the target directory
        assert not Path(target_dir, 'file1.txt').exists()
        assert not Path(target_dir, 'file2.docx').exists()