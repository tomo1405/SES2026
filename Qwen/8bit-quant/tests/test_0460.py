import pytest
from src_0460 import task_func
import os
import time
from datetime import datetime

def test_task_func_negative_delay():
    with pytest.raises(ValueError) as excinfo:
        task_func("/path/to/scripts", ["script1.sh"], -1)
    assert str(excinfo.value) == "delay cannot be negative."

def test_task_func_no_scripts():
    with pytest.raises(ValueError) as excinfo:
        task_func("/path/to/scripts", [], 1)
    assert str(excinfo.value) == "No scripts provided."

def test_task_func_script_not_found(mocker):
    mocker.patch('subprocess.call', return_value=1)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("/path/to/scripts", ["non_existent_script.sh"], 1)
    assert str(excinfo.value) == "Script not found: /path/to/scripts/non_existent_script.sh"

def test_task_func_success(mocker):
    mocker.patch('subprocess.call', return_value=0)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mocker.patch('datetime.datetime.now', return_value=datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S"))
    start_times = task_func("/path/to/scripts", ["script1.sh"], 0)
    assert start_times == [current_time]

def test_task_func_with_delay(mocker):
    mocker.patch('subprocess.call', return_value=0)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mocker.patch('datetime.datetime.now', return_value=datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S"))
    start_times = task_func("/path/to/scripts", ["script1.sh"], 1)
    assert start_times == [current_time]
    time.sleep(1.1)  # Ensure the sleep is completed
    assert datetime.now() >= datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S") + timedelta(seconds=1)