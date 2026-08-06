import pytest
from src_0023 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    K = 5
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert task_func(l1, l2, K) == expected

def test_task_func_with_different_lengths():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9]
    K = 5
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert task_func(l1, l2, K) == expected

def test_task_func_with_empty_lists():
    l1 = []
    l2 = []
    K = 5
    expected = {}
    assert task_func(l1, l2, K) == expected

def test_task_func_with_K_greater_than_length_of_lists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    K = 100
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
    assert task_func(l1, l2, K) == expected