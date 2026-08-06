import pytest
from src_0017 import task_func
import os
import glob
import tempfile
import shutil

def test_task_func_no_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')

def test_task_func_no_logs():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == "No logs found to backup"

def test_task_func_with_logs():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some log files
        log_files = [os.path.join(temp_dir, f'log_{i}.log') for i in range(3)]
        for log_file in log_files:
            with open(log_file, 'w') as f:
                f.write('Log content')

        # Define backup directory
        backup_dir = os.path.join(temp_dir, 'backup')

        # Run the function
        result = task_func(temp_dir, backup_dir=backup_dir)

        # Check if backup file exists
        assert os.path.isfile(result)

        # Check if original log files are removed
        for log_file in log_files:
            assert not os.path.isfile(log_file)

        # Check if backup file contains all log files
        with tarfile.open(result, 'r:gz') as tar:
            tar_contents = tar.getnames()
            for log_file in log_files:
                relative_path = os.path.relpath(log_file, temp_dir)
                assert relative_path in tar_contents

def test_task_func_backup_dir_creation():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define a non-existent backup directory
        backup_dir = os.path.join(temp_dir, 'nonexistent_backup')

        # Create some log files
        log_file = os.path.join(temp_dir, 'log.log')
        with open(log_file, 'w') as f:
            f.write('Log content')

        # Run the function
        task_func(temp_dir, backup_dir=backup_dir)

        # Check if backup directory is created
        assert os.path.isdir(backup_dir)