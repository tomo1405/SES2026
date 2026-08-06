import pytest
from src_0013 import task_func
import os
import json
from datetime import datetime

def test_task_func_script_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_name='non_existent_script.sh')
    assert str(excinfo.value) == "Script non_existent_script.sh does not exist."

def test_task_func_success(mocker):
    mock_subprocess_call = mocker.patch('subprocess.call', return_value=0)
    mock_datetime_now = mocker.patch('datetime.datetime.now')
    start_time = datetime(2023, 10, 1, 12, 0, 0)
    end_time = datetime(2023, 10, 1, 12, 1, 0)
    mock_datetime_now.side_effect = [start_time, end_time]

    log_data = task_func()

    assert log_data['start_time'] == start_time.strftime('%Y-%m-%d %H:%M:%S')
    assert log_data['end_time'] == end_time.strftime('%Y-%m-%d %H:%M:%S')
    assert log_data['exit_status'] == 0

    with open('/home/user/backup_log.json', 'r') as f:
        saved_log_data = json.load(f)
    assert saved_log_data == log_data

def test_task_func_failure(mocker):
    mock_subprocess_call = mocker.patch('subprocess.call', side_effect=subprocess.CalledProcessError(1, 'backup.sh'))
    mock_datetime_now = mocker.patch('datetime.datetime.now')
    start_time = datetime(2023, 10, 1, 12, 0, 0)
    end_time = datetime(2023, 10, 1, 12, 1, 0)
    mock_datetime_now.side_effect = [start_time, end_time]

    with pytest.raises(RuntimeError) as excinfo:
        task_func()
    assert str(excinfo.value) == "Failed to run backup.sh: Command '['./backup.sh']' returned non-zero exit status 1."

    with open('/home/user/backup_log.json', 'r') as f:
        saved_log_data = json.load(f)
    assert saved_log_data['start_time'] == start_time.strftime('%Y-%m-%d %H:%M:%S')
    assert saved_log_data['end_time'] == end_time.strftime('%Y-%m-%d %H:%M:%S')
    assert saved_log_data['exit_status'] == 1