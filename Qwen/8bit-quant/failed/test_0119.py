import pytest
from src_0119 import task_func
import os
import shutil
import tempfile

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as directory:
        with tempfile.TemporaryDirectory() as backup_directory:
            assert task_func(directory, backup_directory) == []

def test_task_func_with_json_files():
    with tempfile.TemporaryDirectory() as directory:
        with tempfile.TemporaryDirectory() as backup_directory:
            # Create some JSON files in the source directory
            json_files = ['file1.json', 'file2.json']
            for file in json_files:
                with open(os.path.join(directory, file), 'w') as f:
                    f.write('{"key": "value"}')

            copied_files = task_func(directory, backup_directory)
            expected_files = [os.path.join(backup_directory, file) for file in json_files]

            assert set(copied_files) == set(expected_files)
            for file in json_files:
                assert os.path.exists(os.path.join(backup_directory, file))

def test_task_func_backup_directory_already_exists():
    with tempfile.TemporaryDirectory() as directory:
        with tempfile.TemporaryDirectory() as backup_directory:
            # Create a JSON file in the source directory
            json_file = 'file1.json'
            with open(os.path.join(directory, json_file), 'w') as f:
                f.write('{"key": "value"}')

            # Ensure the backup directory exists
            os.makedirs(backup_directory)

            copied_files = task_func(directory, backup_directory)
            expected_files = [os.path.join(backup_directory, json_file)]

            assert copied_files == expected_files
            assert os.path.exists(os.path.join(backup_directory, json_file))

def test_task_func_no_directory():
    with tempfile.TemporaryDirectory() as backup_directory:
        with pytest.raises(FileNotFoundError):
            task_func('non_existent_directory', backup_directory)

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as directory:
        with tempfile.TemporaryDirectory() as backup_directory:
            assert task_func(directory, backup_directory) == []