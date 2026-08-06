import pytest
from src_0460 import task_func
import os
import subprocess
import time
from datetime import datetime

def test_task_func_valid_input(mocker):
    # Mocking subprocess.call to avoid actual script execution
    mocker.patch('subprocess.call', return_value=0)
    
    script_dir = '/path/to/scripts'
    scripts = ['script1.sh', 'script2.sh']
    delay = 1
    
    start_times = task_func(script_dir, scripts, delay)
    
    assert len(start_times) == 2
    for start_time in start_times:
        assert datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")

def test_task_func_negative_delay():
    with pytest.raises(ValueError) as excinfo:
        task_func('/path/to/scripts', ['script1.sh'], -1)
    assert str(excinfo.value) == "delay cannot be negative."

def test_task_func_no_scripts():
    with pytest.raises(ValueError) as excinfo:
        task_func('/path/to/scripts', [], 1)
    assert str(excinfo.value) == "No scripts provided."

def test_task_func_script_not_found(mocker):
    # Mocking subprocess.call to simulate script not found
    mocker.patch('subprocess.call', return_value=1)
    
    script_dir = '/path/to/scripts'
    scripts = ['nonexistent_script.sh']
    delay = 1
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(script_dir, scripts, delay)
    assert str(excinfo.value) == "Script not found: /path/to/scripts/nonexistent_script.sh"

def test_task_func_delay_between_scripts(mocker):
    # Mocking subprocess.call to avoid actual script execution
    mocker.patch('subprocess.call', return_value=0)
    
    script_dir = '/path/to/scripts'
    scripts = ['script1.sh', 'script2.sh']
    delay = 1
    
    start_times = task_func(script_dir, scripts, delay)
    
    first_run_time = datetime.strptime(start_times[0], "%Y-%m-%d %H:%M:%S")
    second_run_time = datetime.strptime(start_times[1], "%Y-%m-%d %H:%M:%S")
    
    # Check if there's at least a delay between the two runs
    assert (second_run_time - first_run_time).total_seconds() >= delay