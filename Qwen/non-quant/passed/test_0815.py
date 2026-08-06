import pytest
from src_0815 import task_func
import os
import shutil
import tempfile

def test_task_func_no_source_directory():
    with pytest.raises(FileNotFoundError, match="The source directory does not exist."):
        task_func('nonexistent_source', 'target')

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        assert task_func(source_dir, target_dir) == 0

def test_task_func_move_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        open(os.path.join(source_dir, 'file1.txt'), 'w').close()
        open(os.path.join(source_dir, 'file2.doc'), 'w').close()
        open(os.path.join(source_dir, 'file3.pdf'), 'w').close()

        # Only file1.txt and file2.doc should be moved
        assert task_func(source_dir, target_dir) == 2

        # Check that the files were moved to the target directory
        assert os.path.exists(os.path.join(target_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(target_dir, 'file2.doc'))
        assert not os.path.exists(os.path.join(target_dir, 'file3.pdf'))

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create a file that doesn't match the pattern
        open(os.path.join(source_dir, 'file1.jpg'), 'w').close()

        assert task_func(source_dir, target_dir) == 0

        # Check that no files were moved to the target directory
        assert len(os.listdir(target_dir)) == 0

def test_task_func_existing_target_directory():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        # Create some files in the source directory
        open(os.path.join(source_dir, 'file1.txt'), 'w').close()
        open(os.path.join(source_dir, 'file2.doc'), 'w').close()

        # Call the function twice to ensure the target directory is not recreated
        assert task_func(source_dir, target_dir) == 2
        assert task_func(source_dir, target_dir) == 0