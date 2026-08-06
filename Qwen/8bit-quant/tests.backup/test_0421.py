import pytest
from src_0421 import task_func
import pandas as pd
import numpy as np

# Helper function to check if two DataFrames are approximately equal
def assert_frame_equal(df1, df2):
    pd.testing.assert_frame_equal(df1.round(5), df2.round(5))

def test_task_func_with_numeric_columns():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    expected_output = pd.DataFrame({
        'A': [-1.22474, 0., 1.22474],
        'B': [-1.22474, 0., 1.22474]
    })
    result = task_func(data)
    assert_frame_equal(result, expected_output)

def test_task_func_with_mixed_columns():
    data = {
        'A': [1, 2, 3],
        'B': ['4', '5', '6']
    }
    expected_output = pd.DataFrame({
        'A': [-1.22474, 0., 1.22474],
        'B': [-1.22474, 0., 1.22474]
    })
    result = task_func(data)
    assert_frame_equal(result, expected_output)

def test_task_func_with_non_numeric_columns():
    data = {
        'A': ['a', 'b', 'c'],
        'B': [4, 5, 6]
    }
    expected_output = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [-1.22474, 0., 1.22474]
    })
    result = task_func(data)
    assert_frame_equal(result, expected_output)

def test_task_func_with_empty_dataframe():
    data = {}
    expected_output = pd.DataFrame()
    result = task_func(data)
    assert_frame_equal(result, expected_output)

def test_task_func_with_single_column():
    data = {
        'A': [1, 2, 3]
    }
    expected_output = pd.DataFrame({
        'A': [-1.22474, 0., 1.22474]
    })
    result = task_func(data)
    assert_frame_equal(result, expected_output)

def test_task_func_with_all_nan_values():
    data = {
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    }
    expected_output = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    })
    result = task_func(data)
    assert_frame_equal(result, expected_output)