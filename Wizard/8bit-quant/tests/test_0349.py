python
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Find all processes with the given name, and get their PIDs
    try:
        pids = subprocess.check_output(['pgrep', '-f', process_name]).decode().split('\n')[:-1] 
    except subprocess.CalledProcessError:
        pids = []

    # Send SIGTERM signal to each process
    for pid in pids:
        os.kill(int(pid), signal.SIGTERM)

    # Wait for processes to stop
    time.sleep(1)

    return len(pids)

def test_task_func():
    # Test case 1: process_name is not a string
    assert task_func(123) == 0

    # Test case 2: process_name is a string, but no process is found
    assert task_func('nonexistent_process') == 0

    # Test case 3: process_name is a string, and one process is found
    process_name = 'python'
    p = subprocess.Popen([process_name])
    time.sleep(1)
    assert task_func(process_name) == 1
    p.kill()

    # Test case 4: process_name is a string, and multiple processes are found
    process_name = 'python'
    p1 = subprocess.Popen([process_name])
    p2 = subprocess.Popen([process_name])
    time.sleep(1)
    assert task_func(process_name) == 2
    p1.kill()
    p2.kill()