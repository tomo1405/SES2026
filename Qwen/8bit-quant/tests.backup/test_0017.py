import pytest
from src_0017 import task_func
import os
import glob
import tempfile
import tarfile

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')

def test_task_func_no_logs_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == "No logs found to backup"

def test_task_func_backup_creation():
    with tempfile.TemporaryDirectory() as temp_dir, tempfile.TemporaryDirectory() as backup_dir:
        # Create some log files
        log_files = [os.path.join(temp_dir, f'log_{i}.log') for i in range(3)]
        for log_file in log_files:
            with open(log_file, 'w') as f:
                f.write('Log content')

        backup_file = task_func(temp_dir, backup_dir)
        expected_backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')

        assert backup_file == expected_backup_file
        assert os.path.exists(expected_backup_file)

        # Check if the original log files are removed
        for log_file in log_files:
            assert not os.path.exists(log_file)

        # Check if the backup file contains the correct log files
        with tarfile.open(expected_backup_file, 'r:gz') as tar:
            members = tar.getnames()
            for log_file in log_files:
                relative_path = os.path.relpath(log_file, temp_dir)
                assert relative_path in members

def test_task_func_backup_dir_creation():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some log files
        log_files = [os.path.join(temp_dir, f'log_{i}.log') for i in range(3)]
        for log_file in log_files:
            with open(log_file, 'w') as f:
                f.write('Log content')

        backup_dir = os.path.join(temp_dir, 'backup')
        task_func(temp_dir, backup_dir)

        assert os.path.exists(backup_dir)