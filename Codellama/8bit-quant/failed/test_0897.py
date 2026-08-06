import pytest
from src_0897 import task_func

def test_task_func():
    length = 5
    count = 10
    seed = 0
    expected_result = {'a': 2, 'b': 3, 'c': 1, 'd': 1, 'e': 1}
    assert task_func(length, count, seed) == expected_result

def test_task_func_different_seed():
    length = 5
    count = 10
    seed = 1
    expected_result = {'a': 2, 'b': 3, 'c': 1, 'd': 1, 'e': 1}
    assert task_func(length, count, seed) == expected_result

def test_task_func_different_length():
    length = 10
    count = 10
    seed = 0
    expected_result = {'a': 2, 'b': 3, 'c': 1, 'd': 1, 'e': 1}
    assert task_func(length, count, seed) == expected_result

def test_task_func_different_count():
    length = 5
    count = 20
    seed = 0
    expected_result = {'a': 2, 'b': 3, 'c': 1, 'd': 1, 'e': 1}
    assert task_func(length, count, seed) == expected_result