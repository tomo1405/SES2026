import pytest
from src_1105 import task_func
import subprocess
import threading
import os

def test_task_func_success():
    script_path = 'test_script.py'
    result = task_func(script_path=script_path)
    assert "executed successfully" in result

def test_task_func_timeout():
    script_path = 'nonexistent_script.py'
    result = task_func(script_path=script_path, timeout=1)
    assert "terminating" in result

def test_task_func_subprocess_error():
    script_path = 'nonexistent_script.py'
    result = task_func(script_path=script_path)
    assert "terminating" in result