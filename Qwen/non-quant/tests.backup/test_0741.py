import pytest
from src_0741 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == []

def test_task_func_with_single_letter():
    assert task_func({'a': 1}) == ['a']

def test_task_func_with_multiple_letters():
    assert task_func({'a': 5, 'b': 3, 'c': 8}) == ['c', 'a', 'b']

def test_task_func_with_tie_in_frequency():
    assert task_func({'a': 5, 'b': 5, 'c': 3}) in [['a', 'b'], ['b', 'a']]

def test_task_func_with_all_letters():
    input_dict = {letter: i for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}
    assert task_func(input_dict) == ['z', 'y', 'x']

def test_task_func_with_non_alpha_keys():
    assert task_func({'a': 1, 123: 4, '!': 5}) == ['a']