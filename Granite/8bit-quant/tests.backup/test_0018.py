import subprocess
import psutil
import time
import pytest

def task_func(process_name: str) -> str:
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    
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
    process_name = "example_process"
    
    # Test when the process is running
    def mock_process_iter(*args, **kwargs):
        return [psutil.Process(1234)]
    
    with pytest.patch("psutil.process_iter", side_effect=mock_process_iter):
        result = task_func(process_name)
        assert result == f"Process found. Restarting {process_name}."
    
    # Test when the process is not running
    def mock_process_iter_empty(*args, **kwargs):
        return []
    
    with pytest.patch("psutil.process_iter", side_effect=mock_process_iter_empty):
        result = task_func(process_name)
        assert result == f"Process not found. Starting {process_name}."