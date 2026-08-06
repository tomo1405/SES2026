import pytest
from src_0739 import task_func
import numpy as np

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = 2
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_empty_list():
    L = []
    expected_result = 0
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_single_element_list():
    L = [1]
    expected_result = 0
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_negative_values():
    L = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    expected_result = 2
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_positive_values():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = 2
    actual_result = task_func(L)
    assert actual_result == expected_result

def test_task_func_with_mixed_values():
    L = [[1, -2, 3], [4, -5, 6], [7, -8, 9]]
    expected_result = 2
    actual_result = task_func(L)
    assert actual_result == expected_result