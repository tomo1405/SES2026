import pytest
from src_0349 import task_func

def test_task_func_with_no_processes():
    # Test with no processes
    assert task_func('non_existent_process') == 0

def test_task_func_with_one_process():
    # Test with one process
    assert task_func('python') == 1

def test_task_func_with_multiple_processes():
    # Test with multiple processes
    assert task_func('python') == 2