import pytest
from src_0155 import task_func
import os
import tempfile
import glob
import mimetypes

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, '*.txt', 'txt')
        assert result == {}

def test_task_func_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.txt')
        with open(file_path, 'w') as f:
            f.write('Test content')

        result = task_func(temp_dir, '*.txt', 'txt')
        expected = {file_path: 'text/plain'}
        assert result == expected

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = [os.path.join(temp_dir, f'test{i}.txt') for i in range(3)]
        for file_path in file_paths:
            with open(file_path, 'w') as f:
                f.write(f'Test content {file_path}')

        result = task_func(temp_dir, '*.txt', 'txt')
        expected = {file_path: 'text/plain' for file_path in file_paths}
        assert result == expected

def test_task_func_no_matching_suffix():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.docx')
        with open(file_path, 'w') as f:
            f.write('Test content')

        result = task_func(temp_dir, '*.docx', 'txt')
        assert result == {}

def test_task_func_non_text_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.bin')
        with open(file_path, 'wb') as f:
            f.write(b'\x00\x01\x02\x03')

        result = task_func(temp_dir, '*.bin', 'bin')
        expected = {file_path: 'application/octet-stream'}
        assert result == expected

def test_task_func_directory_not_exists():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent_directory', '*.txt', 'txt')