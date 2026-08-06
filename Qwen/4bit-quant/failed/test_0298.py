import pytest
from src_0298 import task_func

def test_task_func_with_empty_list():
    assert task_func([], 1) == collections.Counter()

def test_task_func_with_single_element():
    assert task_func([1], 1) == collections.Counter({1: 1})

def test_task_func_with_two_elements():
    assert task_func([1, 2], 1) == collections.Counter({1: 1, 2: 1})
    assert task_func([1, 2], 2) == collections.Counter({3: 1})

def test_task_func_with_three_elements():
    assert task_func([1, 2, 3], 1) == collections.Counter({1: 1, 2: 1, 3: 1})
    assert task_func([1, 2, 3], 2) == collections.Counter({3: 1, 4: 2, 5: 1})
    assert task_func([1, 2, 3], 3) == collections.Counter({6: 1})

def test_task_func_with_duplicates():
    assert task_func([1, 1, 1], 1) == collections.Counter({1: 3})
    assert task_func([1, 1, 1], 2) == collections.Counter({2: 3})
    assert task_func([1, 1, 1], 3) == collections.Counter({3: 1})

def test_task_func_with_larger_subset_size():
    assert task_func([1, 2, 3, 4], 4) == collections.Counter({10: 1})
    assert task_func([1, 2, 3, 4], 5) == collections.Counter()

def test_task_func_with_zero_subset_size():
    assert task_func([1, 2, 3], 0) == collections.Counter({0: 1})

def test_task_func_with_negative_elements():
    assert task_func([-1, -2, -3], 1) == collections.Counter({-1: 1, -2: 1, -3: 1})
    assert task_func([-1, -2, -3], 2) == collections.Counter({-3: 1, -4: 2, -5: 1})
    assert task_func([-1, -2, -3], 3) == collections.Counter({-6: 1})