import pytest
from src_0814 import task_func
import pandas as pd

def test_task_func_no_valid_combination():
    number_list = [1, 2, 3]
    element = 10
    result = task_func(number_list, element)
    assert result.empty

def test_task_func_single_valid_combination():
    number_list = [1, 2, 3, 4]
    element = 9
    expected_df = pd.DataFrame({'Combinations': [(2, 3, 4)]})
    result = task_func(number_list, element)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_multiple_valid_combinations():
    number_list = [1, 2, 3, 4, 5]
    element = 9
    expected_df = pd.DataFrame({'Combinations': [(2, 3, 4), (1, 3, 5)]})
    result = task_func(number_list, element)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_duplicate_combinations():
    number_list = [1, 2, 3, 3, 4]
    element = 6
    expected_df = pd.DataFrame({'Combinations': [(1, 2, 3)]})
    result = task_func(number_list, element)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

def test_task_func_empty_number_list():
    number_list = []
    element = 5
    result = task_func(number_list, element)
    assert result.empty

def test_task_func_all_elements_same():
    number_list = [5, 5, 5, 5]
    element = 15
    expected_df = pd.DataFrame({'Combinations': [(5, 5, 5)]})
    result = task_func(number_list, element)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)