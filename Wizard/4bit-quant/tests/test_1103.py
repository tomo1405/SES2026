python
import subprocess
import shlex
from datetime import datetime
import pytest

def task_func(script_path: str) -> dict:
    start_time = datetime.now()
    process = subprocess.Popen(shlex.split(f"/usr/bin/Rscript --vanilla {script_path}"),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = datetime.now()

    log_details = {
        'Start Time': str(start_time),
        'End Time': str(end_time),
        'Stdout': stdout.decode('utf-8'),
        'Stderr': stderr.decode('utf-8')
    }
    
    return log_details

def test_task_func():
    script_path = 'script.R'
    log_details = task_func(script_path)

    assert isinstance(log_details, dict)
    assert 'Start Time' in log_details
    assert 'End Time' in log_details
    assert 'Stdout' in log_details
    assert 'Stderr' in log_details
    assert isinstance(log_details['Start Time'], str)
    assert isinstance(log_details['End Time'], str)
    assert isinstance(log_details['Stdout'], str)
    assert isinstance(log_details['Stderr'], str)