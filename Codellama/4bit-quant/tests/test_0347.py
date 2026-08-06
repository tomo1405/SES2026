import subprocess

import pytest
from src_0347 import task_func


def test_task_func_valid_script():
    script_path = "path/to/script.py"
    args = ["arg1", "arg2"]
    returncode = task_func(script_path, wait=True, *args)
    assert returncode == 0

def test_task_func_invalid_script():
    script_path = "path/to/invalid_script.py"
    with pytest.raises(ValueError):
        task_func(script_path, wait=True)

def test_task_func_exception():
    script_path = "path/to/script.py"
    args = ["arg1", "arg2"]
    with pytest.raises(subprocess.CalledProcessError):
        task_func(script_path, wait=True, *args)