python
import subprocess
import os
import signal
import time

from src_0349 import task_func

def test_task_func():
    # Test case 1: No process with given name
    assert task_func('nonexistent_process') == 0

    # Test case 2: One process with given name
    process = subprocess.Popen(['sleep', '10'])
    assert task_func('sleep') == 1
    process.kill()

    # Test case 3: Multiple processes with given name
    process1 = subprocess.Popen(['sleep', '10'])
    process2 = subprocess.Popen(['sleep', '10'])
    assert task_func('sleep') == 2
    process1.kill()
    process2.kill()