python
import subprocess
import psutil
import time

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

# Test the function with pytest
import pytest

def test_task_func():
    # Test case 1: process is running, terminate it and restart
    process_name = "chrome.exe"
    subprocess.Popen(process_name)
    assert task_func(process_name) == f"Process found. Restarting {process_name}."
    
    # Test case 2: process is not running, start it
    process_name = "notepad.exe"
    subprocess.Popen(process_name)
    assert task_func(process_name) == f"Process not found. Starting {process_name}."