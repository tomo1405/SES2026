python
import subprocess
import os
import json
from datetime import datetime
import pytest

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    log_data = {}

    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"Script {script_name} does not exist.")

    start_time = datetime.now()
    log_data['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        exit_status = subprocess.call(['./' + script_name])
    except Exception as e:
        raise RuntimeError(f"Failed to run {script_name}: {str(e)}")

    end_time = datetime.now()
    log_data['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    log_data['exit_status'] = exit_status

    with open(log_file, 'w') as f:
        json.dump(log_data, f)
    
    return log_data

def test_task_func():
    # Test case 1: script file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(script_name='invalid_script.sh')

    # Test case 2: script file exists, but fails to run
    with pytest.raises(RuntimeError):
        task_func(script_name='failing_script.sh')

    # Test case 3: script file exists and runs successfully
    log_data = task_func(script_name='backup.sh')
    assert isinstance(log_data, dict)
    assert 'start_time' in log_data
    assert 'end_time' in log_data
    assert 'exit_status' in log_data