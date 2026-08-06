python
import subprocess
import os
import sys
import time

from src_0347 import task_func

def test_task_func():
    # Test with valid script path
    script_path = "test_script.py"
    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")
    assert task_func(script_path) == 0
    os.remove(script_path)

    # Test with invalid script path
    script_path = "invalid_script.py"
    try:
        task_func(script_path)
    except ValueError as e:
        assert str(e) == f"Script '{script_path}' does not exist."

    # Test with wait=False
    script_path = "test_script.py"
    with open(script_path, "w") as f:
        f.write("import time\ntime.sleep(5)")
    process = task_func(script_path, wait=False)
    assert process.poll() is None
    os.remove(script_path)

    # Test with args
    script_path = "test_script.py"
    with open(script_path, "w") as f:
        f.write("import sys\nprint(sys.argv)")
    assert task_func(script_path, "arg1", "arg2") == 0
    os.remove(script_path)

    # Test with exception in script
    script_path = "test_script.py"
    with open(script_path, "w") as f:
        f.write("raise Exception('Test exception')")
    try:
        task_func(script_path)
    except subprocess.CalledProcessError as e:
        assert e.returncode == 1
        assert e.cmd == [sys.executable, script_path]
    os.remove(script_path)