import pytest
from src_0769 import task_func
import os
import tempfile
import glob

def test_task_func_non_existent_directory():
    with pytest.raises(ValueError) as excinfo:
        task_func('non_existent_directory')
    assert str(excinfo.value) == "Specified directory does not exist."

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_single_file_no_errors():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'file.txt')
        with open(file_path, 'w') as file:
            file.write('This is a test file without errors.')
        result = task_func(temp_dir)
        assert result == {'file.txt': 0}

def test_task_func_single_file_with_errors():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'file.txt')
        with open(file_path, 'w') as file:
            file.write('This is a test file with an error and another Error.')
        result = task_func(temp_dir)
        assert result == {'file.txt': 2}

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path1 = os.path.join(temp_dir, 'file1.txt')
        file_path2 = os.path.join(temp_dir, 'file2.txt')
        with open(file_path1, 'w') as file:
            file.write('This is a test file with an error.')
        with open(file_path2, 'w') as file:
            file.write('This is another test file with another Error.')
        result = task_func(temp_dir)
        assert result == {'file1.txt': 1, 'file2.txt': 1}

def test_task_func_nested_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        sub_dir = os.path.join(temp_dir, 'subdir')
        os.makedirs(sub_dir)
        file_path1 = os.path.join(sub_dir, 'file1.txt')
        file_path2 = os.path.join(sub_dir, 'file2.txt')
        with open(file_path1, 'w') as file:
            file.write('This is a test file with an error.')
        with open(file_path2, 'w') as file:
            file.write('This is another test file with another Error.')
        result = task_func(temp_dir)
        assert result == {'subdir/file1.txt': 1, 'subdir/file2.txt': 1}