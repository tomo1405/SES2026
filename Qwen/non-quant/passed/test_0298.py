import pytest
from src_0298 import task_func
import itertools
import collections

def test_task_func_empty_list():
    elements = []
    subset_size = 0
    expected = collections.Counter()
    assert task_func(elements, subset_size) == expected

def test_task_func_single_element():
    elements = [1]
    subset_size = 1
    expected = collections.Counter([1])
    assert task_func(elements, subset_size) == expected

def test_task_func_multiple_elements():
    elements = [1, 2, 3]
    subset_size = 2
    expected = collections.Counter({3: 1, 4: 1, 5: 1})
    assert task_func(elements, subset_size) == expected

def test_task_func_no_subsets():
    elements = [1, 2, 3]
    subset_size = 0
    expected = collections.Counter([0])
    assert task_func(elements, subset_size) == expected

def test_task_func_larger_subset_size():
    elements = [1, 2, 3, 4]
    subset_size = 3
    expected = collections.Counter({6: 1, 7: 2, 8: 2, 9: 1})
    assert task_func(elements, subset_size) == expected

def test_task_func_negative_elements():
    elements = [-1, -2, -3]
    subset_size = 2
    expected = collections.Counter({-3: 1, -4: 1, -5: 1})
    assert task_func(elements, subset_size) == expected

def test_task_func_mixed_elements():
    elements = [-1, 0, 1]
    subset_size = 2
    expected = collections.Counter({-1: 1, 0: 1, 1: 1})
    assert task_func(elements, subset_size) == expected