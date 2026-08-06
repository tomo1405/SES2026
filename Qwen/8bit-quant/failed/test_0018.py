import pytest
from src_0018 import task_func
import psutil
import subprocess

def test_task_func_process_running(mocker):
    process_name = "test_process"
    
    # Mock to simulate the process is running
    mocker.patch('psutil.process_iter', return_value=[mocker.Mock(name=process_name)])
    mocker.patch.object(psutil.Process, 'terminate')
    mocker.patch('subprocess.Popen')
    
    result = task_func(process_name)
    
    assert result == f"Process found. Restarting {process_name}."
    psutil.Process.terminate.assert_called_once()
    subprocess.Popen.assert_called_once_with(process_name)

def test_task_func_process_not_running(mocker):
    process_name = "test_process"
    
    # Mock to simulate the process is not running
    mocker.patch('psutil.process_iter', return_value=[])
    mocker.patch('subprocess.Popen')
    
    result = task_func(process_name)
    
    assert result == f"Process not found. Starting {process_name}."
    subprocess.Popen.assert_called_once_with(process_name)

def test_task_func_no_processes(mocker):
    process_name = "test_process"
    
    # Mock to simulate no processes are returned
    mocker.patch('psutil.process_iter', return_value=[])
    mocker.patch('subprocess.Popen')
    
    result = task_func(process_name)
    
    assert result == f"Process not found. Starting {process_name}."
    subprocess.Popen.assert_called_once_with(process_name)

def test_task_func_multiple_processes(mocker):
    process_name = "test_process"
    
    # Mock to simulate multiple processes with the same name
    mock_proc1 = mocker.Mock(name=process_name)
    mock_proc2 = mocker.Mock(name=process_name)
    mocker.patch('psutil.process_iter', return_value=[mock_proc1, mock_proc2])
    mocker.patch.object(psutil.Process, 'terminate')
    mocker.patch('subprocess.Popen')
    
    result = task_func(process_name)
    
    assert result == f"Process found. Restarting {process_name}."
    assert psutil.Process.terminate.call_count == 2
    subprocess.Popen.assert_called_once_with(process_name)