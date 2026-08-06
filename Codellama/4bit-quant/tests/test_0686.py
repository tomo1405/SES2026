from typing import Counter

from src_0686 import task_func


def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = Counter([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert task_func(list_of_lists) == expected_result

def test_task_func_empty_list():
    list_of_lists = []
    expected_result = Counter()
    assert task_func(list_of_lists) == expected_result

def test_task_func_single_list():
    list_of_lists = [[1, 2, 3]]
    expected_result = Counter([1, 2, 3])
    assert task_func(list_of_lists) == expected_result

def test_task_func_duplicate_elements():
    list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    expected_result = Counter([1, 2, 3, 4, 5])
    assert task_func(list_of_lists) == expected_result