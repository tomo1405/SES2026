import pytest
from src_0349 import task_func
import subprocess
import os
import signal
import time

def test_task_func_no_processes(mocker):
    # Mock subprocess.check_output to return no processes
    mocker.patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(1, 'pgrep'))
    
    result = task_func('non_existent_process')
    assert result == 0

def test_task_func_one_process(mocker):
    # Mock subprocess.check_output to return one process
    mocker.patch('subprocess.check_output', return_value=b'1234\n')
    
    result = task_func('existing_process')
    assert result == 1

def test_task_func_multiple_processes(mocker):
    # Mock subprocess.check_output to return multiple processes
    mocker.patch('subprocess.check_output', return_value=b'1234\n5678\n')
    
    result = task_func('existing_process')
    assert result == 2

def test_task_func_process_killing(mocker):
    # Mock subprocess.check_output to return one process
    mocker.patch('subprocess.check_output', return_value=b'1234\n')
    
    # Mock os.kill to avoid actually killing processes
    mock_kill = mocker.patch('os.kill')
    
    result = task_func('existing_process')
    mock_kill.assert_called_once_with(1234, signal.SIGTERM)
    assert result == 1

def test_task_func_sleep_duration(mocker):
    # Mock subprocess.check_output to return one process
    mocker.patch('subprocess.check_output', return_value=b'1234\n')
    
    # Mock time.sleep to avoid actual sleep
    mock_sleep = mocker.patch('time.sleep')
    
    result = task_func('existing_process')
    mock_sleep.assert_called_once_with(1)
    assert result == 1