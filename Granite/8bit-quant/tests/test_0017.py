import os
import glob
import subprocess
from unittest import mock

def task_func(directory, backup_dir='/path/to/backup'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")

    log_files = glob.glob(os.path.join(directory, '*.log'))
    if not log_files:
        return "No logs found to backup"

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    subprocess.call(['tar', '-czvf', backup_file] + log_files)

    for file in log_files:
        os.remove(file)

    return backup_file

def test_task_func():
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        assert task_func('/path/to/directory') == '/path/to/backup/logs_backup.tar.gz'
        mock_exists.assert_has_calls([
            mock.call('/path/to/directory'),
            mock.call('/path/to/backup'),
        ])

    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.side_effect = [False, True]
        with pytest.raises(FileNotFoundError):
            task_func('/path/to/directory')
        mock_exists.assert_has_calls([
            mock.call('/path/to/directory'),
            mock.call('/path/to/backup'),
        ])

    with mock.patch('os.path.exists') as mock_exists, mock.patch('os.makedirs') as mock_makedirs:
        mock_exists.side_effect = [True, False]
        task_func('/path/to/directory')
        mock_exists.assert_has_calls([
            mock.call('/path/to/directory'),
            mock.call('/path/to/backup'),
        ])
        mock_makedirs.assert_called_once_with('/path/to/backup')

    with mock.patch('os.path.exists') as mock_exists, mock.patch('glob.glob') as mock_glob:
        mock_exists.return_value = True
        mock_glob.return_value = []
        assert task_func('/path/to/directory') == "No logs found to backup"
        mock_exists.assert_has_calls([
            mock.call('/path/to/directory'),
            mock.call('/path/to/backup'),
        ])
        mock_glob.assert_called_once_with('/path/to/directory/*.log')

    with mock.patch('os.path.exists') as mock_exists, mock.patch('glob.glob') as mock_glob, mock.patch('subprocess.call') as mock_call, mock.patch('os.remove') as mock_remove:
        mock_exists.return_value = True
        mock_glob.return_value = ['/path/to/directory/log1.log', '/path/to/directory/log2.log']
        task_func('/path/to/directory')
        mock_exists.assert_has_calls([
            mock.call('/path/to/directory'),
            mock.call('/path/to/backup'),
        ])
        mock_glob.assert_called_once_with('/path/to/directory/*.log')
        mock_call.assert_called_once_with(['tar', '-czvf', '/path/to/backup/logs_backup.tar.gz', '/path/to/directory/log1.log', '/path/to/directory/log2.log'])
        mock_remove.assert_has_calls([
            mock.call('/path/to/directory/log1.log'),
            mock.call('/path/to/directory/log2.log'),
        ])