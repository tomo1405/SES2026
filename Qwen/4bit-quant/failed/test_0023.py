import pytest
from src_0023 import task_func
from collections import Counter
from itertools import zip_longest
from random import seed

def test_task_func_with_equal_lists():
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7, 8]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=8)
    assert isinstance(result, Counter)
    assert len(result) <= 8
    assert all(isinstance(key, int) and key in range(1, 9) for key in result)

def test_task_func_with_unequal_lists():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7, 8]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=10)
    assert isinstance(result, Counter)
    assert len(result) <= 10
    assert all(isinstance(key, int) and key in range(1, 9) for key in result)

def test_task_func_with_empty_list():
    l1 = []
    l2 = [1, 2, 3]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=5)
    assert isinstance(result, Counter)
    assert len(result) <= 5
    assert all(isinstance(key, int) and key in range(1, 4) for key in result)

def test_task_func_with_all_none():
    l1 = [None, None, None]
    l2 = [None, None, None]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=5)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_single_element():
    l1 = [1]
    l2 = [2]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=1)
    assert isinstance(result, Counter)
    assert len(result) == 1
    assert 1 in result or 2 in result

def test_task_func_with_large_K():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    seed(0)  # For reproducibility
    result = task_func(l1, l2, K=100)
    assert isinstance(result, Counter)
    assert len(result) <= 6  # Since there are only 6 elements in total

def test_task_func_with_zero_K():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    result = task_func(l1, l2, K=0)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_negative_K():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    with pytest.raises(ValueError):
        task_func(l1, l2, K=-1)