import pytest
from src_0023 import task_func

def test_task_func():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = 2
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
    assert task_func(l1, l2, K) == expected

def test_task_func_empty_lists():
    l1 = []
    l2 = []
    K = 10
    expected = {}
    assert task_func(l1, l2, K) == expected

def test_task_func_different_lengths():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]
    K = 10
    expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
    assert task_func(l1, l2, K) == expected

def test_task_func_invalid_K():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = 0
    with pytest.raises(ValueError):
        task_func(l1, l2, K)