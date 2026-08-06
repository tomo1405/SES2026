import pytest
from src_0022 import task_func

def test_task_func_os():
    result = task_func()
    assert 'OS' in result
    assert result['OS'] == platform.system()

def test_task_func_architecture():
    result = task_func()
    assert 'Architecture' in result
    assert result['Architecture'] == platform.architecture()[0]

def test_task_func_memory_usage():
    result = task_func()
    assert 'Memory Usage' in result
    memory_usage = result['Memory Usage']
    assert isinstance(memory_usage, str)
    percentage = float(memory_usage.strip('%'))
    assert 0 <= percentage <= 100