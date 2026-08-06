import pytest
from src_0668 import task_func

def test_task_func_with_unique_elements():
    x = [1, 2, 3, 4, 5]
    n = 3
    assert task_func(x, n) == [1, 2, 3]

def test_task_func_with_repeated_elements():
    x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    n = 3
    assert task_func(x, n) == [1, 2, 3]

def test_task_func_with_all_elements_same():
    x = [1, 1, 1, 1, 1]
    n = 2
    assert task_func(x, n) == [1]

def test_task_func_with_n_greater_than_unique_elements():
    x = [1, 2, 3]
    n = 5
    assert task_func(x, n) == [1, 2, 3]

def test_task_func_with_empty_list():
    x = []
    n = 3
    assert task_func(x, n) == []

def test_task_func_with_single_element():
    x = [1]
    n = 1
    assert task_func(x, n) == [1]

def test_task_func_with_negative_numbers():
    x = [-1, -2, -3, -1, -2, -1]
    n = 2
    assert task_func(x, n) == [-1, -2]

def test_task_func_with_mixed_types():
    x = [1, 'a', 'a', 2, 2, 2, 3]
    n = 3
    assert task_func(x, n) == [2, 'a', 3]