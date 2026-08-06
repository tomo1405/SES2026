import subprocess
import os
import signal
import time
import pytest

def task_func(process_name: str) -> int:
    try:
        pids = subprocess.check_output(['pgrep', '-f', process_name]).decode().split('\n')[:-1] 
    except subprocess.CalledProcessError:
        pids = []

    for pid in pids:
        os.kill(int(pid), signal.SIGTERM)

    time.sleep(1)

    return len(pids)

def test_task_func():
    process_name = "example_process"
    num_processes_before = task_func(process_name)
    subprocess.Popen([process_name])
    time.sleep(1)
    num_processes_after = task_func(process_name)
    assert num_processes_after == num_processes_before + 1

def test_task_func_no_processes():
    process_name = "nonexistent_process"
    num_processes_before = task_func(process_name)
    time.sleep(1)
    num_processes_after = task_func(process_name)
    assert num_processes_after == num_processes_before