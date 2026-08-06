python
import subprocess
import os
import sys
import time

from src_0347 import task_func

def test_task_func():
    # Test if script exists
    script_path = "script.py"
    assert os.path.isfile(script_path)

    # Test running script in a background process
    args = ["arg1", "arg2"]
    process = subprocess.Popen(
        [sys.executable, script_path, *args], 
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    assert "Exception" not in str(process.communicate()[1])

    # Test waiting for the process to complete
    task_func(script_path, wait=True, *args)
    assert process.poll() is not None

    # Test not waiting for the process to complete
    task_func(script_path, wait=False, *args)
    assert process.poll() is None