import pytest
from src_0017 import task_func
import os
import tempfile

def test_task_func_no_logs_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == "No logs found to backup"

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/non/existing/directory')
    assert str(excinfo.value) == "Directory '/non/existing/directory' not found."

def test_task_func_success():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some log files
        with open(os.path.join(temp_dir, 'file1.log'), 'w') as f:
            f.write('Log content 1')
        with open(os.path.join(temp_dir, 'file2.log'), 'w') as f:
            f.write('Log content 2')

        backup_dir = tempfile.mkdtemp()
        result = task_func(temp_dir, backup_dir=backup_dir)

        assert os.path.exists(result)
        assert not os.path.exists(os.path.join(temp_dir, 'file1.log'))
        assert not os.path.exists(os.path.join(temp_dir, 'file2.log'))

def test_task_func_backup_dir_created():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some log files
        with open(os.path.join(temp_dir, 'file1.log'), 'w') as f:
            f.write('Log content 1')

        backup_dir = os.path.join(temp_dir, 'backup')
        result = task_func(temp_dir, backup_dir=backup_dir)

        assert os.path.exists(backup_dir)
        assert os.path.exists(result)
        assert not os.path.exists(os.path.join(temp_dir, 'file1.log'))