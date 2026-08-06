import pytest
from src_0859 import task_func

def test_task_func():
    n = 10
    seed = 42
    expected_result = {'l': 3, 'e': 2, 'r': 2, 'n': 1, 'a': 1, 's': 1, 'g': 1, 't': 1, 'i': 1, 'c': 1}
    result = task_func(n, seed)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_default_seed():
    n = 10
    expected_result = {'l': 4, 'e': 3, 'r': 2, 'n': 1, 'a': 1, 's': 1, 'g': 1, 't': 1, 'i': 1, 'c': 1}
    result = task_func(n)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_zero_n():
    n = 0
    seed = 42
    expected_result = {}
    result = task_func(n, seed)
    assert result == expected_result, "Task function returned an incorrect result"