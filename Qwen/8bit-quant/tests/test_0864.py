import pytest
from src_0864 import task_func

def test_task_func_empty_input():
    assert task_func([]) == []

def test_task_func_single_empty_list():
    assert task_func([[]]) == [0]

def test_task_func_single_list_with_one_element():
    assert task_func([[1]]) == [1]

def test_task_func_single_list_with_multiple_elements():
    assert task_func([[1, 2]]) == [1 + 4]

def test_task_func_multiple_lists():
    assert task_func([[1], [2, 3], [4, 5, 6]]) == [1, 1 + 4, 1 + 4 + 9]

def test_task_func_lists_with_different_lengths():
    assert task_func([[1], [2, 3, 4], [5, 6, 7, 8, 9]]) == [1, 1 + 4 + 9, 1 + 4 + 9 + 16 + 25]

def test_task_func_large_numbers():
    assert task_func([[10, 10], [10, 10, 10]]) == [1 + 4, 1 + 4 + 9]

def test_task_func_all_possible_numbers():
    assert task_func([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100]