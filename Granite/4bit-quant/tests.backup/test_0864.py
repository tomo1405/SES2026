import pytest
from src_0864 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
    expected_result = [55, 55, 225]

    result = task_func(list_of_lists)

    assert result == expected_result

def test_task_func_with_empty_list():
    list_of_lists = [[]]
    expected_result = [0]

    result = task_func(list_of_lists)

    assert result == expected_result

def test_task_func_with_lists_of_different_lengths():
    list_of_lists = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
    expected_result = [55, 140, 170]

    result = task_func(list_of_lists)

    assert result == expected_result