import pytest
from src_0551 import task_func
from collections import Counter
import pandas as pd

def test_task_func_with_empty_list():
    input_data = []
    expected_output = pd.DataFrame(columns=['Count']).rename_axis('MenuItem')
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_single_item():
    input_data = [['burger']]
    expected_output = pd.DataFrame({'Count': [1]}, index=['burger']).rename_axis('MenuItem')
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_multiple_items():
    input_data = [['burger', 'fries'], ['burger', 'soda']]
    expected_output = pd.DataFrame({'Count': [2, 1, 1]}, index=['burger', 'fries', 'soda']).rename_axis('MenuItem')
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_duplicates_in_sublists():
    input_data = [['burger', 'burger'], ['fries', 'fries', 'fries']]
    expected_output = pd.DataFrame({'Count': [2, 3]}, index=['burger', 'fries']).rename_axis('MenuItem')
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_different_items():
    input_data = [['pizza'], ['pasta', 'salad'], ['pizza', 'salad', 'salad']]
    expected_output = pd.DataFrame({'Count': [2, 1, 3]}, index=['pizza', 'pasta', 'salad']).rename_axis('MenuItem')
    assert task_func(input_data).equals(expected_output)