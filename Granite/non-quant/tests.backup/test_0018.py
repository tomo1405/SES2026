import subprocess
import psutil
import time
import pytest

def task_func(process_name: str) -> str:
    # Check if the process is running
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    
    # If the process is running, terminate it
    if is_running:
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.terminate()
                time.sleep(5)
        subprocess.Popen(process_name)
        return f"Process found. Restarting {process_name}."
    else:
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."

def test_task_func():
    # Test case 1: Process is running
    def mock_process_iter():
        class MockProcess:
            def __init__(self, name):
                self.name = name
        return [MockProcess(process_name)]
    
    with patch('psutil.process_iter', side_effect=mock_process_iter):
        result = task_func(process_name)
        assert result == f"Process found. Restarting {process_name}."
    
    # Test case 2: Process is not running
    def mock_process_iter():
        return []
    
    with patch('psutil.process_iter', side_effect=mock_process_iter):
        result = task_func(process_name)
        assert result == f"Process not found. Starting {process_name}."