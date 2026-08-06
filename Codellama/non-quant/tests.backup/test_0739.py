import pytest
from src_0739 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = 3
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_empty_list():
    L = []
    expected_result = None
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_invalid_input():
    L = "invalid input"
    expected_result = None
    actual_result = task_func(L)
    assert actual_result == expected_result