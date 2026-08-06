import pytest
from src_0576 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_empty_list():
    """
    Test task_func with an empty list
    """
    expected_output = pd.DataFrame()
    actual_output = task_func([])
    assert actual_output.equals(expected_output)

def test_task_func_with_one_element_list():
    """
    Test task_func with a list containing only one element
    """
    expected_output = pd.DataFrame([[1]])
    actual_output = task_func([1])
    assert actual_output.equals(expected_output)

def test_task_func_with_multiple_elements_list():
    """
    Test task_func with a list containing multiple elements
    """
    expected_output = pd.DataFrame([[4, 3, 2, 1, 0], [3, 2, 1, 0, 4], [2, 1, 0, 4, 3], [1, 0, 4, 3, 2], [0, 4, 3, 2, 1]])
    actual_output = task_func([0, 1, 2, 3, 4])
    assert actual_output.equals(expected_output)

def test_task_func_with_n_groups_greater_than_list_length():
    """
    Test task_func with n_groups greater than the length of the input list
    """
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0]])
    actual_output = task_func([0], n_groups=5)
    assert actual_output.equals(expected_output)

def test_task_func_with_n_groups_less_than_list_length():
    """
    Test task_func with n_groups less than the length of the input list
    """
    expected_output = pd.DataFrame([[4, 3, 2, 1, 0], [3, 2, 1, 0, 4], [2, 1, 0, 4, 3], [1, 0, 4, 3, 2], [0, 4, 3, 2, 1]])
    actual_output = task_func([0, 1, 2, 3, 4], n_groups=4)
    assert actual_output.equals(expected_output)