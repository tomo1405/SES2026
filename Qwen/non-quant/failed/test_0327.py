import pytest
from src_0327 import task_func
import os
import tempfile
import subprocess

def test_task_func_no_bat_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []

def test_task_func_one_bat_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_path = os.path.join(temp_dir, 'test.bat')
        with open(bat_file_path, 'w') as f:
            f.write('@echo off\nexit /b 0')

        result = task_func(temp_dir)
        assert result == [('test.bat', 0)]

def test_task_func_multiple_bat_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_paths = [os.path.join(temp_dir, f'test{i}.bat') for i in range(3)]
        for bat_file_path in bat_file_paths:
            with open(bat_file_path, 'w') as f:
                f.write('@echo off\nexit /b 0')

        result = task_func(temp_dir)
        expected_results = [(os.path.basename(path), 0) for path in bat_file_paths]
        assert result == expected_results

def test_task_func_bat_file_with_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_path = os.path.join(temp_dir, 'test.bat')
        with open(bat_file_path, 'w') as f:
            f.write('@echo off\nexit /b 1')

        result = task_func(temp_dir)
        assert result == [('test.bat', 1)]

def test_task_func_non_executable_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_executable_file_path = os.path.join(temp_dir, 'test.txt')
        with open(non_executable_file_path, 'w') as f:
            f.write('This is a text file.')

        result = task_func(temp_dir)
        assert result == []

def test_task_func_permission_denied():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_path = os.path.join(temp_dir, 'test.bat')
        with open(bat_file_path, 'w') as f:
            f.write('@echo off\nexit /b 0')

        # Change permissions to make the file non-executable
        os.chmod(bat_file_path, 0o444)

        result = task_func(temp_dir)
        assert len(result) == 1
        assert result[0][0] == 'test.bat'
        assert result[0][1] is None