import os
from unittest.mock import call, patch

import pytest
from src_0017 import task_func


def test_task_func_with_valid_directory():
    with patch('os.path.exists') as mock_exists, \
         patch('glob.glob') as mock_glob, \
         patch('os.makedirs') as mock_makedirs, \
         patch('subprocess.call') as mock_call, \
         patch('os.remove') as mock_remove:
        mock_exists.side_effect = [True, False]
        mock_glob.return_value = ['/path/to/log1.log', '/path/to/log2.log']
        backup_file = task_func('/path/to/directory')
        mock_exists.assert_has_calls([
            call('/path/to/directory'),
            call('/path/to/backup')
        ])
        mock_glob.assert_called_with(os.path.join('/path/to/directory', '*.log'))
        mock_makedirs.assert_called_with('/path/to/backup')
        mock_call.assert_has_calls([
            call(['tar', '-czvf', '/path/to/backup/logs_backup.tar.gz', '/path/to/log1.log', '/path/to/log2.log']),
            call(['rm', '/path/to/log1.log']),
            call(['rm', '/path/to/log2.log'])
        ])
        mock_remove.assert_has_calls([
            call('/path/to/log1.log'),
            call('/path/to/log2.log')
        ])
        assert backup_file == '/path/to/backup/logs_backup.tar.gz'

def test_task_func_with_invalid_directory():
    with patch('os.path.exists') as mock_exists:
        mock_exists.side_effect = [False]
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func('/path/to/directory')
        assert str(excinfo.value) == "Directory '/path/to/directory' not found."
        mock_exists.assert_called_with('/path/to/directory')

def test_task_func_with_no_log_files():
    with patch('os.path.exists') as mock_exists, \
         patch('glob.glob') as mock_glob:
        mock_exists.side_effect = [True, False]
        mock_glob.return_value = []
        result = task_func('/path/to/directory')
        mock_exists.assert_has_calls([
            call('/path/to/directory'),
            call('/path/to/backup')
        ])
        mock_glob.assert_called_with(os.path.join('/path/to/directory', '*.log'))
        assert result == "No logs found to backup"