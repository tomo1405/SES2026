import subprocess
import os
import sys
import time
import pytest
from src_0347 import task_func

def test_task_func_valid_script():
    script_path = "path/to/valid/script.py"
    with pytest.raises(ValueError) as excinfo:
        task_func(script_path)
    assert "Script 'path/to/valid/script.py' does not exist." in str(excinfo.value)

def test_task_func_invalid_script():
    script_path = "path/to/invalid/script.py"
    with pytest.raises(subprocess.CalledProcessError) as excinfo:
        task_func(script_path)
    assert "Exception" in str(excinfo.value)

def test_task_func_wait():
    script_path = "path/to/valid/script.py"
    result = task_func(script_path, wait=True)
    assert result == 0

def test_task_func_nowait():
    script_path = "path/to/valid/script.py"
    result = task_func(script_path, wait=False)
    assert result is None