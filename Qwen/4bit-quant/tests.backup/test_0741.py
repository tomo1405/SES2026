import pytest
from src_0741 import task_func

def test_task_func_with_empty_dict():
    assert task_func({}) == []

def test_task_func_with_single_letter():
    assert task_func({'a': 1}) == ['a']

def test_task_func_with_multiple_same_letters():
    assert task_func({'a': 5, 'b': 5, 'c': 5}) == ['a', 'b', 'c']

def test_task_func_with_less_than_three_letters():
    assert task_func({'a': 1, 'b': 2}) == ['b', 'a']

def test_task_func_with_more_than_three_letters():
    assert task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == ['d', 'c', 'b']

def test_task_func_with_mixed_case():
    assert task_func({'a': 1, 'B': 2, 'c': 3}) == ['c', 'a', 'B']

def test_task_func_with_non_alpha_characters():
    assert task_func({'!': 1, '@': 2, '#': 3}) == []