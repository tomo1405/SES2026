import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def test_task_func_with_valid_data():
    # Test with valid data that matches the pattern
    df = pd.DataFrame({
        'A': ['>1.23<', '>4.56<', None],
        'B': ['>7.89<', '>0.12<', '>3.45<']
    })
    expected_df = pd.DataFrame({
        'A': [1.23, 4.56, np.nan],
        'B': [7.89, 0.12, 3.45]
    })
    result_df = task_func(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_no_match():
    # Test with data that does not match the pattern
    df = pd.DataFrame({
        'A': ['1.23', '4.56', None],
        'B': ['7.89', '0.12', '3.45']
    })
    expected_df = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    })
    result_df = task_func(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_empty_dataframe():
    # Test with an empty DataFrame
    df = pd.DataFrame()
    expected_df = pd.DataFrame()
    result_df = task_func(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_single_column():
    # Test with a single column DataFrame
    df = pd.DataFrame({
        'A': ['>1.23<', '>4.56<', None]
    })
    expected_df = pd.DataFrame({
        'A': [1.23, 4.56, np.nan]
    })
    result_df = task_func(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_all_null_values():
    # Test with a DataFrame where all values are None
    df = pd.DataFrame({
        'A': [None, None, None],
        'B': [None, None, None]
    })
    expected_df = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    })
    result_df = task_func(df)
    pd.testing.assert_frame_equal(result_df, expected_df)