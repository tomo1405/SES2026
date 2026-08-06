import pytest
from src_0828 import task_func

def test_task_func():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [2, 3, 5, 7]
    actual_output = task_func(input_list)
    assert actual_output == expected_output

def test_task_func_empty_input():
    input_list = []
    expected_output = []
    actual_output = task_func(input_list)
    assert actual_output == expected_output

def test_task_func_single_element_input():
    input_list = [1]
    expected_output = [1]
    actual_output = task_func(input_list)
    assert actual_output == expected_output

def test_task_func_duplicate_elements_input():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [2, 3, 5, 7]
    actual_output = task_func(input_list)
    assert actual_output == expected_output

def test_task_func_invalid_input():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c"]
    expected_output = [2, 3, 5, 7]
    actual_output = task_func(input_list)
    assert actual_output == expected_output