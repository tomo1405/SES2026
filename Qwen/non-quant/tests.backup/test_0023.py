import pytest
from src_0023 import task_func
from collections import Counter
from itertools import zip_longest
from random import choices

def test_task_func_empty_lists():
    assert task_func([], []) == Counter()

def test_task_func_single_element_lists():
    assert task_func([1], [2]) == Counter({1: 1, 2: 1})

def test_task_func_unbalanced_lists():
    result = task_func([1, 2, 3], [4])
    assert all(key in result for key in [1, 2, 3, 4])

def test_task_func_identical_lists():
    result = task_func([1, 2, 3], [1, 2, 3])
    assert all(key in result for key in [1, 2, 3])

def test_task_func_large_K():
    result = task_func([1, 2, 3], [4, 5, 6], K=100)
    assert sum(result.values()) == 100

def test_task_func_zero_K():
    assert task_func([1, 2, 3], [4, 5, 6], K=0) == Counter()

def test_task_func_negative_K():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], [4, 5, 6], K=-1)

def test_task_func_with_none_values():
    result = task_func([1, None, 3], [None, 5, 6])
    assert None not in result

def test_task_func_with_duplicates():
    result = task_func([1, 1, 2], [2, 3, 3])
    assert all(key in result for key in [1, 2, 3])