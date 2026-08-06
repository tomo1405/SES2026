import pytest
from src_0013 import task_func
import subprocess
import os
import json
from datetime import datetime

def test_task_func_success():
    # Test successful execution
    script_name = 'test_script.sh'
    log_file = 'test_log.json'
    result = task_func(script_name=script_name, log_file=log_file)
    
    assert 'start_time' in result
    assert 'end_time' in result
    assert 'exit_status' in result
    assert os.path.isfile(log_file)
    
    # Clean up the log file
    os.remove(log_file)

def test_task_func_file_not_found():
    script_name = 'nonexistent_script.sh'
    log_file = 'test_log.json'
    with pytest.raises(FileNotFoundError):
        task_func(script_name=script_name, log_file=log_file)

def test_task_func_script_execution_error():
    script_name = 'nonexistent_script.sh'
    log_file = 'test_log.json'
    with pytest.raises(RuntimeError):
        task_func(script_name=script_name, log_file=log_file)