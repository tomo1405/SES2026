import pytest
from src_0347 import task_func
import subprocess
import os
import sys
import time

def test_task_func_valid_script():
    script_path = "valid_script.py"
    result = task_func(script_path=script_path)
    assert result is not None

def test_task_func_invalid_script():
    script_path = "nonexistent_script.py"
    with pytest.raises(ValueError):
        task_func(script_path=script_path)

def test_task_func_wait_false():
    script_path = "valid_script.py"
    result = task_func(script_path=script_path, wait=False)
    assert result is None