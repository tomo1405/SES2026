import pytest
from src_0814 import task_func

def test_task_func():
    number_list = [1, 2, 3, 4, 5]
    element = 6
    expected_output = pd.DataFrame({'Combinations': [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]})
    actual_output = task_func(number_list, element)
    assert actual_output.equals(expected_output)

def test_task_func_empty_list():
    number_list = []
    element = 0
    expected_output = pd.DataFrame({'Combinations': []})
    actual_output = task_func(number_list, element)
    assert actual_output.equals(expected_output)

def test_task_func_no_combinations():
    number_list = [1, 2, 3, 4, 5]
    element = 1
    expected_output = pd.DataFrame({'Combinations': []})
    actual_output = task_func(number_list, element)
    assert actual_output.equals(expected_output)