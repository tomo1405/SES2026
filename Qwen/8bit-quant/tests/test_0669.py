import pytest
from src_0669 import task_func

def test_task_func_empty_dict():
    assert task_func({}) == []

def test_task_func_single_element():
    assert task_func({'a': 5}) == ['a']

def test_task_func_multiple_elements():
    assert task_func({'a': 5, 'b': 3, 'c': 8}) == ['b']

def test_task_func_equal_lengths():
    assert task_func({'a': 5, 'b': 5}) == ['a', 'b']

def test_task_func_negative_lengths():
    assert task_func({'a': -1, 'b': -2, 'c': -3}) == ['a', 'b', 'c']

def test_task_func_mixed_lengths():
    assert task_func({'a': 10, 'b': 1, 'c': 2, 'd': 3}) == ['b']

def test_task_func_large_numbers():
    assert task_func({'a': 10**6, 'b': 10**5, 'c': 10**4}) == ['c']