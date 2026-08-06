python
import subprocess
import os
import signal
import time

from src_0349 import task_func

def test_task_func():
    # Test case 1: process_name is not running
    process_name = 'nonexistent_process'
    assert task_func(process_name) == 0

    # Test case 2: process_name is running
    process_name = 'python'
    p = subprocess.Popen([process_name])
    time.sleep(1)
    assert task_func(process_name) == 1
    p.kill()