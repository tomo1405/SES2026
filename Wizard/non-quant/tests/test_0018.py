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
def test_task_func():
    # Test case 1: process is running, terminate it and restart
    assert task_func("chrome.exe") == "Process found. Restarting chrome.exe."
    
    # Test case 2: process is not running, start it
    assert task_func("notepad.exe") == "Process not found. Starting notepad.exe."