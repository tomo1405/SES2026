import os
import tempfile

import pytest
from src_0643 import task_func


def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_single_file_matching_pattern():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "AcroTray.exe")
        with open(test_file_path, 'wb') as f:
            f.write(b"test data")
        
        result = task_func(temp_dir)
        assert len(result) == 1
        assert test_file_path in result
        assert isinstance(result[test_file_path], str)

def test_task_func_single_file_not_matching_pattern():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "DistillrAcroTray.exe")
        with open(test_file_path, 'wb') as f:
            f.write(b"test data")
        
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = [
            os.path.join(temp_dir, "AcroTray.exe"),
            os.path.join(temp_dir, "DistillrAcroTray.exe"),
            os.path.join(temp_dir, "AcroTray2.exe")
        ]
        for file_path in file_paths:
            with open(file_path, 'wb') as f:
                f.write(b"test data")
        
        result = task_func(temp_dir)
        assert len(result) == 2
        for file_path in file_paths[:2]:
            assert file_path in result
            assert isinstance(result[file_path], str)

def test_task_func_invalid_directory():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_directory")