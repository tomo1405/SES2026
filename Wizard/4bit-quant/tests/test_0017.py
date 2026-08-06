python
import os
import glob
import subprocess
import pytest

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
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('/path/to/nonexistent/directory')

    # Test case 2: Directory contains no log files
    assert task_func('/path/to/empty/directory') == "No logs found to backup"

    # Test case 3: Directory contains log files
    directory = '/path/to/directory/with/logs'
    backup_dir = '/path/to/backup'
    os.makedirs(directory)
    with open(os.path.join(directory, 'log1.log'), 'w') as f:
        f.write('log1')
    with open(os.path.join(directory, 'log2.log'), 'w') as f:
        f.write('log2')
    backup_file = task_func(directory, backup_dir)
    assert os.path.exists(backup_file)
    assert os.path.isfile(backup_file)
    assert os.path.getsize(backup_file) > 0
    os.remove(backup_file)
    os.rmdir(directory)
    os.rmdir(backup_dir)