import pytest
from src_0669 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == []

def test_task_func_with_single_element():
    assert task_func({'a': 5}) == ['a']

def test_task_func_with_two_elements():
    assert task_func({'a': 5, 'b': 3}) == ['b']

def test_task_func_with_three_elements():
    assert task_func({'a': 5, 'b': 3, 'c': 2}) == ['c']

def test_task_func_with_equal_lengths():
    assert task_func({'a': 5, 'b': 5, 'c': 5}) == ['a'] or ['b'] or ['c']

def test_task_func_with_multiple_minimal_subsequences():
    assert task_func({'a': 5, 'b': 3, 'c': 3, 'd': 1}) == ['d']

def test_task_func_with_negative_lengths():
    assert task_func({'a': -1, 'b': -2, 'c': -3}) == ['a']

def test_task_func_with_mixed_positive_and_negative_lengths():
    assert task_func({'a': 5, 'b': -2, 'c': 3}) == ['b']