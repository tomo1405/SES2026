import pytest
from src_0119 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary directory with some JSON files
    with tempfile.TemporaryDirectory() as temp_dir:
        json_files = ['file1.json', 'file2.txt', 'file3.json']
        for file in json_files:
            open(os.path.join(temp_dir, file), 'a').close()

        # Create a temporary backup directory
        with tempfile.TemporaryDirectory() as backup_dir:
            # Call the function
            result = task_func(temp_dir, backup_dir)

            # Check if only JSON files were copied
            assert len(result) == 2
            assert all(file.endswith('.json') for file in result)

            # Check if the files exist in the backup directory
            for file in result:
                assert os.path.exists(file)

            # Check if non-JSON files were not copied
            for file in json_files:
                if not file.endswith('.json'):
                    assert not os.path.exists(os.path.join(backup_dir, file))

def test_task_func_non_existent_directory():
    # Create a temporary directory with some JSON files
    with tempfile.TemporaryDirectory() as temp_dir:
        json_files = ['file1.json', 'file2.txt', 'file3.json']
        for file in json_files:
            open(os.path.join(temp_dir, file), 'a').close()

        # Use a non-existent directory for backup
        backup_dir = os.path.join(temp_dir, 'non_existent_backup')

        # Call the function
        result = task_func(temp_dir, backup_dir)

        # Check if only JSON files were copied
        assert len(result) == 2
        assert all(file.endswith('.json') for file in result)

        # Check if the backup directory was created
        assert os.path.exists(backup_dir)

        # Check if the files exist in the backup directory
        for file in result:
            assert os.path.exists(file)

def test_task_func_no_json_files():
    # Create a temporary directory with no JSON files
    with tempfile.TemporaryDirectory() as temp_dir:
        non_json_files = ['file1.txt', 'file2.docx']
        for file in non_json_files:
            open(os.path.join(temp_dir, file), 'a').close()

        # Create a temporary backup directory
        with tempfile.TemporaryDirectory() as backup_dir:
            # Call the function
            result = task_func(temp_dir, backup_dir)

            # Check if no files were copied
            assert len(result) == 0

            # Check if no files exist in the backup directory
            for file in non_json_files:
                assert not os.path.exists(os.path.join(backup_dir, file))