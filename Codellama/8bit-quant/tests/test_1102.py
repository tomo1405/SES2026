import pytest
from src_1102 import task_func

def test_task_func():
    test_dir = 'path/to/test/directory'
    execution_times = task_func(test_dir)
    assert isinstance(execution_times, dict)
    assert all(isinstance(key, str) for key in execution_times.keys())
    assert all(isinstance(value, float) for value in execution_times.values())