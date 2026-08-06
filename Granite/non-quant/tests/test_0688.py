import pytest
from src_0688 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    expected_output = (3, 3)
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output, "Output mismatch"

def test_task_func_with_empty_list():
    list_of_lists = [[]]
    expected_output = (None, 0)
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output, "Output mismatch"

def test_task_func_with_list_of_lists_with_single_item():
    list_of_lists = [[1], [1], [1]]
    expected_output = (1, 3)
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output, "Output mismatch"