import pytest
from src_0023 import task_func
from collections import Counter
from itertools import zip_longest
from random import choices

def test_task_func_empty_lists():
    assert task_func([], []) == Counter()

def test_task_func_single_element_lists():
    assert task_func([1], [2]) == Counter({1: 1, 2: 1})

def test_task_func_different_lengths():
    l1 = [1, 2, 3]
    l2 = [4, 5]
    result = task_func(l1, l2)
    assert all(elem in result for elem in l1 + l2)
    assert len(result) <= 10

def test_task_func_identical_lists():
    l = [1, 2, 3]
    result = task_func(l, l)
    assert result == Counter({1: 2, 2: 2, 3: 2})

def test_task_func_large_lists():
    l1 = list(range(100))
    l2 = list(range(50, 150))
    result = task_func(l1, l2)
    assert all(elem in result for elem in l1 + l2)
    assert len(result) <= 10

def test_task_func_custom_K():
    l1 = [1, 2, 3]
    l2 = [4, 5]
    result = task_func(l1, l2, K=5)
    assert len(result) <= 5

def test_task_func_none_values():
    l1 = [1, None, 3]
    l2 = [None, 5, 6]
    result = task_func(l1, l2)
    assert 1 in result and 3 in result and 5 in result and 6 in result
    assert None not in result