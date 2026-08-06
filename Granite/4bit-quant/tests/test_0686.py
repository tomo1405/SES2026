import pytest
from src_0686 import task_func
from collections import Counter
from itertools import chain

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output

def test_task_func_with_empty_list():
    list_of_lists = [[], [4, 5, 6], [7, 8, 9]]
    expected_output = Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output

def test_task_func_with_nested_lists():
    list_of_lists = [[1, 2, [3]], [4, 5, 6], [7, 8, 9]]
    expected_output = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output