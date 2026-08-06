import subprocess
import time

import psutil
from src_0018 import task_func


def test_task_func_running():
    # Setup
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    if not is_running:
        subprocess.Popen(process_name)
        time.sleep(5)

    # Test
    result = task_func(process_name)

    # Assert
    assert result == f"Process found. Restarting {process_name}."

def test_task_func_not_running():
    # Setup
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    if is_running:
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                proc.terminate()
                time.sleep(5)

    # Test
    result = task_func(process_name)

    # Assert
    assert result == f"Process not found. Starting {process_name}."