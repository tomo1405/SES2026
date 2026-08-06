import pytest
from src_0349 import task_func

def test_task_func():
    # Test case 1: no processes with the given name
    process_name = 'test_process'
    pids = []
    assert task_func(process_name) == 0

    # Test case 2: one process with the given name
    process_name = 'test_process'
    pids = [1234]
    assert task_func(process_name) == 1

    # Test case 3: multiple processes with the given name
    process_name = 'test_process'
    pids = [1234, 5678, 9012]
    assert task_func(process_name) == 3

    # Test case 4: invalid process name
    process_name = 'invalid_process'
    pids = []
    assert task_func(process_name) == 0