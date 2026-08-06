import pytest
from src_0669 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == []

def test_task_func_with_single_element():
    assert task_func({'a': 5}) == ['a']

def test_task_func_with_multiple_elements():
    assert task_func({'a': 3, 'b': 2, 'c': 1}) == ['c']

def test_task_func_with_equal_lengths():
    assert task_func({'a': 2, 'b': 2, 'c': 2}) == ['a']

def test_task_func_with_large_numbers():
    assert task_func({'x': 1000, 'y': 500, 'z': 250}) == ['z']

def test_task_func_with_negative_lengths():
    with pytest.raises(ValueError):
        task_func({'a': -1, 'b': -2})

def test_task_func_with_zero_length():
    with pytest.raises(ValueError):
        task_func({'a': 0, 'b': 0})