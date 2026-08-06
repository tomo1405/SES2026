import pytest
from src_0864 import task_func

def test_task_func_with_empty_list():
    assert task_func([]) == []

def test_task_func_with_single_empty_list():
    assert task_func([[]]) == [0]

def test_task_func_with_single_list():
    assert task_func([[1]]) == [1]

def test_task_func_with_multiple_lists():
    assert task_func([[1, 2], [3]]) == [5, 9]

def test_task_func_with_full_length_list():
    assert task_func([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [385]

def test_task_func_with_max_length_list():
    assert task_func([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9]]) == [385, 285]

def test_task_func_with_zero_length_list():
    assert task_func([[], []]) == [0, 0]

def test_task_func_with_negative_numbers():
    assert task_func([[-1, -2], [-3]]) == [5, 9]

def test_task_func_with_large_numbers():
    assert task_func([[100, 200], [300]]) == [385, 9]