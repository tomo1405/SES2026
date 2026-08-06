import pytest
from src_0814 import task_func
import pandas as pd

def test_task_func_no_valid_combination():
    number_list = [1, 2, 3, 4]
    element = 10
    result = task_func(number_list, element)
    assert result.empty, "Expected an empty DataFrame for no valid combinations"

def test_task_func_single_valid_combination():
    number_list = [1, 2, 3, 4]
    element = 6
    expected_output = pd.DataFrame({'Combinations': [(1, 2, 3)]})
    result = task_func(number_list, element)
    assert result.equals(expected_output), f"Expected {expected_output} but got {result}"

def test_task_func_multiple_valid_combinations():
    number_list = [1, 2, 3, 4, 5]
    element = 9
    expected_output = pd.DataFrame({'Combinations': [(1, 2, 6), (1, 3, 5), (2, 3, 4)]})
    result = task_func(number_list, element)
    assert set(result['Combinations']) == set(expected_output['Combinations']), f"Expected {set(expected_output['Combinations'])} but got {set(result['Combinations'])}"

def test_task_func_duplicate_combinations():
    number_list = [1, 2, 2, 3, 4]
    element = 5
    expected_output = pd.DataFrame({'Combinations': [(1, 2, 2)]})
    result = task_func(number_list, element)
    assert result.equals(expected_output), f"Expected {expected_output} but got {result}"

def test_task_func_empty_list():
    number_list = []
    element = 5
    result = task_func(number_list, element)
    assert result.empty, "Expected an empty DataFrame for an empty input list"

def test_task_func_all_zeros():
    number_list = [0, 0, 0, 0]
    element = 0
    expected_output = pd.DataFrame({'Combinations': [(0, 0, 0)]})
    result = task_func(number_list, element)
    assert result.equals(expected_output), f"Expected {expected_output} but got {result}"