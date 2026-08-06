import pytest
from src_0736 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = {'mean': 5, 'variance': 8.666666666666666}
    actual_output = task_func(L)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_empty_list():
    L = [[]]
    expected_output = {'mean': 0, 'variance': 0}
    actual_output = task_func(L)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_one_element_list():
    L = [[1]]
    expected_output = {'mean': 1, 'variance': 0}
    actual_output = task_func(L)
    assert actual_output == expected_output, "Task function returned incorrect output"