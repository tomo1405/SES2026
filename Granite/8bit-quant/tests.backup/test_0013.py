import subprocess
import os
import json
from datetime import datetime
from src_0013 import task_func
import pytest

def test_task_func_with_valid_input():
    script_name = 'backup.sh'
    log_file = '/home/user/backup_log.json'
    log_data = task_func(script_name, log_file)
    assert 'start_time' in log_data
    assert 'end_time' in log_data
    assert 'exit_status' in log_data

def test_task_func_with_invalid_script_name():
    script_name = 'invalid_script.sh'
    log_file = '/home/user/backup_log.json'
    with pytest.raises(FileNotFoundError):
        task_func(script_name, log_file)

def test_task_func_with_invalid_log_file():
    script_name = 'backup.sh'
    log_file = '/invalid/log/file.json'
    with pytest.raises(RuntimeError):
        task_func(script_name, log_file)

def test_task_func_with_invalid_script_and_log_file():
    script_name = 'invalid_script.sh'
    log_file = '/invalid/log/file.json'
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_name, log_file)
    assert 'Script invalid_script.sh does not exist.' in str(excinfo.value)
    with pytest.raises(RuntimeError) as excinfo:
        task_func(script_name, log_file)
    assert 'Failed to run invalid_script.sh' in str(excinfo.value)