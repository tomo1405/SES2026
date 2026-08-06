import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def test_task_func_with_valid_data():
    # Create a sample DataFrame with valid data
    df = pd.DataFrame({
        'A': ['>1.23<', '>4.56<', '>7.89<'],
        'B': ['>10.11<', '>12.13<', '>14.15<']
    })
    
    # Expected output DataFrame
    expected_df = pd.DataFrame({
        'A': [1.23, 4.56, 7.89],
        'B': [10.11, 12.13, 14.15]
    })
    
    # Run the function
    result_df = task_func(df, DATA_PATTERN)
    
    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_missing_data():
    # Create a sample DataFrame with missing data
    df = pd.DataFrame({
        'A': ['>1.23<', np.nan, '>7.89<'],
        'B': ['>10.11<', '>12.13<', np.nan]
    })
    
    # Expected output DataFrame
    expected_df = pd.DataFrame({
        'A': [1.23, np.nan, 7.89],
        'B': [10.11, 12.13, np.nan]
    })
    
    # Run the function
    result_df = task_func(df, DATA_PATTERN)
    
    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_no_matching_pattern():
    # Create a sample DataFrame with no matching pattern
    df = pd.DataFrame({
        'A': ['1.23', '4.56', '7.89'],
        'B': ['10.11', '12.13', '14.15']
    })
    
    # Expected output DataFrame
    expected_df = pd.DataFrame({
        'A': [np.nan, np.nan, np.nan],
        'B': [np.nan, np.nan, np.nan]
    })
    
    # Run the function
    result_df = task_func(df, DATA_PATTERN)
    
    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)