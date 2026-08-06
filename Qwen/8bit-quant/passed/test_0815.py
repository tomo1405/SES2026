import pytest
from src_0815 import task_func
import os
import tempfile
import shutil

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        assert task_func(source_dir, target_dir) == 0

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        files_to_create = ['file1.txt', 'file2.doc', 'file3.pdf', 'file4.docx']
        for file in files_to_create:
            open(os.path.join(source_dir, file), 'a').close()

        # Expected files to be moved
        expected_moved_files = ['file1.txt', 'file2.doc', 'file4.docx']

        # Run the function
        moved_files_count = task_func(source_dir, target_dir)

        # Check if the correct number of files were moved
        assert moved_files_count == len(expected_moved_files)

        # Check if the files were moved to the target directory
        for file in expected_moved_files:
            assert os.path.exists(os.path.join(target_dir, file))

        # Check if the files that were not supposed to be moved are still in the source directory
        for file in files_to_create:
            if file not in expected_moved_files:
                assert os.path.exists(os.path.join(source_dir, file))

def test_task_func_non_existent_source_dir():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(FileNotFoundError):
            task_func('non_existent_source_dir', target_dir)

def test_task_func_target_dir_creation():
    with tempfile.TemporaryDirectory() as source_dir:
        # Create a file in the source directory
        open(os.path.join(source_dir, 'file1.txt'), 'a').close()

        # Path for a non-existent target directory
        target_dir = os.path.join(source_dir, 'non_existent_target_dir')

        # Run the function
        task_func(source_dir, target_dir)

        # Check if the target directory was created
        assert os.path.exists(target_dir)

        # Check if the file was moved to the target directory
        assert os.path.exists(os.path.join(target_dir, 'file1.txt'))