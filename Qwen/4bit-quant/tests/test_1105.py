import pytest
from src_1105 import task_func
import os
import time

def test_task_func_success(tmpdir):
    # Create a simple script that sleeps for 2 seconds and then exits
    script_path = tmpdir.join("success_script.py")
    script_path.write("import time\ntime.sleep(2)\nprint('Success!')\n")

    result = task_func(str(script_path), timeout=5)
    assert result == 'Script executed successfully.'

def test_task_func_timeout(tmpdir):
    # Create a script that runs indefinitely
    script_path = tmpdir.join("timeout_script.py")
    script_path.write("while True:\n    pass\n")

    result = task_func(str(script_path), timeout=2)
    assert result == 'Terminating process due to timeout.'

def test_task_func_nonexistent_script():
    script_path = "nonexistent_script.py"
    result = task_func(script_path, timeout=2)
    assert result == 'Script executed successfully.'  # The script won't run, so it won't exceed the timeout

def test_task_func_zero_timeout(tmpdir):
    # Create a simple script that sleeps for 2 seconds and then exits
    script_path = tmpdir.join("zero_timeout_script.py")
    script_path.write("import time\ntime.sleep(2)\nprint('Success!')\n")

    result = task_func(str(script_path), timeout=0)
    assert result == 'Terminating process due to timeout.'

def test_task_func_negative_timeout(tmpdir):
    # Create a simple script that sleeps for 2 seconds and then exits
    script_path = tmpdir.join("negative_timeout_script.py")
    script_path.write("import time\ntime.sleep(2)\nprint('Success!')\n")

    result = task_func(str(script_path), timeout=-1)
    assert result == 'Terminating process due to timeout.'