import pytest
from src_0859 import task_func

def test_task_func():
    n = 10
    seed = 42
    expected_result = {'e': 2, 'r': 2, 'o': 1, 'm': 1, 't': 1, 'a': 1, 'c': 1, 'i': 1, 'n': 1, 'd': 1}
    result = task_func(n, seed)
    assert result == expected_result

def test_task_func_without_seed():
    n = 10
    expected_result = {'e': 2, 'r': 2, 'o': 1, 'm': 1, 't': 1, 'a': 1, 'c': 1, 'i': 1, 'n': 1, 'd': 1}
    result = task_func(n)
    assert result == expected_result

def test_task_func_with_zero_n():
    n = 0
    seed = 42
    expected_result = {}
    result = task_func(n, seed)
    assert result == expected_result