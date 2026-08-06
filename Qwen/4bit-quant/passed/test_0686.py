import pytest
from src_0686 import task_func
from collections import Counter

def test_task_func_with_empty_lists():
    assert task_func([[], []]) == Counter()

def test_task_func_with_single_element_lists():
    assert task_func([[1], [2]]) == Counter({1: 1, 2: 1})

def test_task_func_with_multiple_elements():
    assert task_func([[1, 2, 3], [4, 5, 6], [1, 2]]) == Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1})

def test_task_func_with_identical_lists():
    assert task_func([[1, 1, 1], [1, 1]]) == Counter({1: 4})

def test_task_func_with_mixed_data_types():
    assert task_func([[1, 'a'], ['b', 1], [1, 'a']]) == Counter({1: 3, 'a': 2, 'b': 1})

def test_task_func_with_negative_numbers():
    assert task_func([[-1, -2], [-2, -3], [-1]]) == Counter({-1: 2, -2: 2, -3: 1})