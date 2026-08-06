import pytest
from src_0327 import task_func
import os
import tempfile
import subprocess

def test_task_func_no_bat_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []

def test_task_func_single_bat_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_path = os.path.join(temp_dir, 'test.bat')
        with open(bat_file_path, 'w') as f:
            f.write('echo Hello, World!')

        result = task_func(temp_dir)
        assert len(result) == 1
        assert result[0][0] == 'test.bat'
        assert result[0][1] == 0

def test_task_func_multiple_bat_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_paths = [os.path.join(temp_dir, f'test_{i}.bat') for i in range(3)]
        for path in bat_file_paths:
            with open(path, 'w') as f:
                f.write('echo Hello, World!')

        result = task_func(temp_dir)
        assert len(result) == 3
        for i, (filename, exit_code) in enumerate(result):
            assert filename == f'test_{i}.bat'
            assert exit_code == 0

def test_task_func_bat_file_with_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        bat_file_path = os.path.join(temp_dir, 'test.bat')
        with open(bat_file_path, 'w') as f:
            f.write('exit /b 1')

        result = task_func(temp_dir)
        assert len(result) == 1
        assert result[0][0] == 'test.bat'
        assert result[0][1] == 1

def test_task_func_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')