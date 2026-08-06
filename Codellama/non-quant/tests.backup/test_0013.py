import pytest
from src_0013 import task_func

def test_task_func_valid_script():
    script_name = 'backup.sh'
    log_file = '/home/user/backup_log.json'
    log_data = task_func(script_name, log_file)
    assert log_data['start_time'] == '2023-02-21 12:00:00'
    assert log_data['end_time'] == '2023-02-21 12:00:00'
    assert log_data['exit_status'] == 0

def test_task_func_invalid_script():
    script_name = 'invalid.sh'
    log_file = '/home/user/backup_log.json'
    with pytest.raises(FileNotFoundError):
        task_func(script_name, log_file)

def test_task_func_exception():
    script_name = 'backup.sh'
    log_file = '/home/user/backup_log.json'
    with pytest.raises(RuntimeError):
        task_func(script_name, log_file)