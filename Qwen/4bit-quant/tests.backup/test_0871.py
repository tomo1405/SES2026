import pytest
from src_0871 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_data():
    expected_df = pd.DataFrame({
        'Mean Value': [np.mean([1, 2, 3, 4, 5]), np.mean([2.1, 3.2, 4.3, 5.4, 6.5])]
    }, index=['Position 0', 'Position 1'])
    result_df = task_func()
    assert result_df.equals(expected_df)

def test_task_func_custom_data():
    custom_data = [('x', 10, 20.5), ('y', 20, 30.5), ('z', 30, 40.5)]
    expected_df = pd.DataFrame({
        'Mean Value': [np.mean([10, 20, 30]), np.mean([20.5, 30.5, 40.5])]
    }, index=['Position 0', 'Position 1'])
    result_df = task_func(custom_data)
    assert result_df.equals(expected_df)

def test_task_func_single_element():
    custom_data = [('single', 100, 200.5)]
    expected_df = pd.DataFrame({
        'Mean Value': [100, 200.5]
    }, index=['Position 0', 'Position 1'])
    result_df = task_func(custom_data)
    assert result_df.equals(expected_df)

def test_task_func_empty_data():
    custom_data = []
    expected_df = pd.DataFrame({'Mean Value': []}, index=[])
    result_df = task_func(custom_data)
    assert result_df.equals(expected_df)

def test_task_func_missing_values():
    custom_data = [('a', 1, None), ('b', None, 3.2), ('c', 3, 4.3), ('d', 4, None), ('e', 5, 6.5)]
    expected_df = pd.DataFrame({
        'Mean Value': [np.mean([1, 3, 4, 5]), np.mean([3.2, 4.3, 6.5])]
    }, index=['Position 0', 'Position 1'])
    result_df = task_func(custom_data)
    assert result_df.equals(expected_df)