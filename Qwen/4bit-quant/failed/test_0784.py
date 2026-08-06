import pytest
from src_0784 import task_func
import os
import tempfile

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        assert task_func(src_dir, dest_dir, '.txt') == 0

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some files in the source directory
        with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
            f.write('content')
        with open(os.path.join(src_dir, 'file2.txt'), 'w') as f:
            f.write('content')
        with open(os.path.join(src_dir, 'file3.log'), 'w') as f:
            f.write('content')

        # Move .txt files to the destination directory
        assert task_func(src_dir, dest_dir, '.txt') == 2

        # Check if the files have been moved correctly
        assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))
        assert not os.path.exists(os.path.join(src_dir, 'file1.txt'))
        assert not os.path.exists(os.path.join(src_dir, 'file2.txt'))

        # Check if the non-matching file is still in the source directory
        assert os.path.exists(os.path.join(src_dir, 'file3.log'))

def test_task_func_empty_extension():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
            f.write('content')
        with open(os.path.join(src_dir, 'file2.log'), 'w') as f:
            f.write('content')

        # Attempt to move files with an empty extension
        assert task_func(src_dir, dest_dir, '') == 0

        # Check if no files have been moved
        assert os.path.exists(os.path.join(src_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(src_dir, 'file2.log'))

def test_task_func_non_existent_src_dir():
    with tempfile.TemporaryDirectory() as dest_dir:
        with pytest.raises(FileNotFoundError):
            task_func('/non/existent/src', dest_dir, '.txt')

def test_task_func_non_existent_dest_dir():
    with tempfile.TemporaryDirectory() as src_dir:
        with pytest.raises(FileNotFoundError):
            task_func(src_dir, '/non/existent/dest', '.txt')