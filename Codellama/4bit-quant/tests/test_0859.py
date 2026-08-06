import pytest
from src_0859 import task_func

def test_task_func():
    n = 10
    seed = 1234
    expected_result = {'a': 2, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
    assert task_func(n, seed) == expected_result

def test_task_func_with_different_seed():
    n = 10
    seed = 5678
    expected_result = {'a': 2, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
    assert task_func(n, seed) == expected_result

def test_task_func_with_different_n():
    n = 20
    seed = 1234
    expected_result = {'a': 2, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
    assert task_func(n, seed) == expected_result

def test_task_func_with_different_n_and_seed():
    n = 20
    seed = 5678
    expected_result = {'a': 2, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
    assert task_func(n, seed) == expected_result