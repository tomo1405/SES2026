import pytest
from src_1105 import task_func

def test_task_func_success():
    script_path = 'test_script.py'
    timeout = 60
    result = task_func(script_path, timeout)
    assert result == 'Script executed successfully.'

def test_task_func_timeout():
    script_path = 'test_script.py'
    timeout = 0.1
    result = task_func(script_path, timeout)
    assert result == 'Terminating process due to timeout.'