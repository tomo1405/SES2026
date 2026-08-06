import pytest
from src_0455 import task_func
import os
import shutil
import tempfile

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        assert task_func(src_dir, dest_dir, 'txt') == []

def test_task_func_single_file():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        file_path = os.path.join(src_dir, 'test.txt')
        with open(file_path, 'w') as f:
            f.write('Test content')
        moved_files = task_func(src_dir, dest_dir, 'txt')
        assert len(moved_files) == 1
        assert moved_files[0] == os.path.join(dest_dir, 'test.txt')
        assert not os.path.exists(file_path)

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        file_paths = [os.path.join(src_dir, f'test{i}.txt') for i in range(3)]
        for file_path in file_paths:
            with open(file_path, 'w') as f:
                f.write('Test content')
        moved_files = task_func(src_dir, dest_dir, 'txt')
        assert len(moved_files) == 3
        for file_path in file_paths:
            assert os.path.join(dest_dir, os.path.basename(file_path)) in moved_files
            assert not os.path.exists(file_path)

def test_task_func_nonexistent_src_dir():
    with tempfile.TemporaryDirectory() as dest_dir:
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func('/nonexistent/src', dest_dir, 'txt')
        assert "Source directory '/nonexistent/src' does not exist." in str(excinfo.value)

def test_task_func_nonexistent_dest_dir():
    with tempfile.TemporaryDirectory() as src_dir:
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(src_dir, '/nonexistent/dest', 'txt')
        assert "Destination directory '/nonexistent/dest' does not exist." in str(excinfo.value)

def test_task_func_different_extensions():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        file_path_txt = os.path.join(src_dir, 'test.txt')
        file_path_py = os.path.join(src_dir, 'test.py')
        with open(file_path_txt, 'w') as f:
            f.write('Test content')
        with open(file_path_py, 'w') as f:
            f.write('Python content')
        moved_files = task_func(src_dir, dest_dir, 'txt')
        assert len(moved_files) == 1
        assert moved_files[0] == os.path.join(dest_dir, 'test.txt')
        assert os.path.exists(file_path_py)