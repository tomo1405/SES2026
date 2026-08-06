import subprocess
import os
import threading
import pytest
from src_1105 import task_func

def test_task_func():
    script_path = 'path/to/script.py'
    timeout = 10  # Set a timeout value for the function

    result = task_func(script_path, timeout)

    assert result == 'Script executed successfully.'

def test_task_func_timeout():
    script_path = 'path/to/script.py'
    timeout = 1  # Set a shorter timeout value for the function

    result = task_func(script_path, timeout)

    assert result == 'Terminating process due to timeout.'