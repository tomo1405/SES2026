import pytest
from src_0975 import task_func
import tempfile
import os

def test_task_func_source_not_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('Hello, World!')
        with pytest.raises(ValueError):
            task_func(file_path, os.path.join(temp_dir, 'destination'))

def test_task_func_destination_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source')
        os.makedirs(source_path)
        with open(os.path.join(source_path, 'file1.txt'), 'w') as f:
            f.write('File 1 content')
        destination_path = os.path.join(temp_dir, 'destination')
        os.makedirs(destination_path)
        result = task_func(source_path, destination_path)
        assert result == ('source', ['file1.txt'])
        assert os.path.exists(os.path.join(destination_path, 'file1.txt'))

def test_task_func_copy_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source')
        os.makedirs(source_path)
        with open(os.path.join(source_path, 'file1.txt'), 'w') as f:
            f.write('File 1 content')
        with open(os.path.join(source_path, 'file2.txt'), 'w') as f:
            f.write('File 2 content')
        destination_path = os.path.join(temp_dir, 'destination')
        result = task_func(source_path, destination_path)
        assert result == ('source', ['file1.txt', 'file2.txt'])
        assert os.path.exists(os.path.join(destination_path, 'file1.txt'))
        assert os.path.exists(os.path.join(destination_path, 'file2.txt'))

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source')
        os.makedirs(source_path)
        destination_path = os.path.join(temp_dir, 'destination')
        result = task_func(source_path, destination_path)
        assert result == ('source', [])
        assert not os.path.exists(os.path.join(destination_path, 'file1.txt'))

def test_task_func_nested_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source')
        os.makedirs(os.path.join(source_path, 'subdir'))
        with open(os.path.join(source_path, 'subdir', 'file1.txt'), 'w') as f:
            f.write('File 1 content')
        destination_path = os.path.join(temp_dir, 'destination')
        result = task_func(source_path, destination_path)
        assert result == ('source', ['file1.txt'])
        assert os.path.exists(os.path.join(destination_path, 'file1.txt'))