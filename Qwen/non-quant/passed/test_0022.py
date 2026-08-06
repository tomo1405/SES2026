import pytest
from src_0022 import task_func
import platform
import psutil

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
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    expected_memory_usage = f'{used_memory/total_memory*100:.2f}%'
    assert result['Memory Usage'] == expected_memory_usage

def test_task_func_keys():
    result = task_func()
    expected_keys = {'OS', 'Architecture', 'Memory Usage'}
    assert set(result.keys()) == expected_keys