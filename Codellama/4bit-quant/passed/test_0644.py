import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test case 1: Test with a valid dataframe
    df = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'], 'B': ['>0.12<', '>3.45<', '>6.78<']})
    expected_df = pd.DataFrame({'A': [1.23, 4.56, 7.89], 'B': [0.12, 3.45, 6.78]})
    result_df = task_func(df)
    assert result_df.equals(expected_df)

    # Test case 2: Test with a dataframe with invalid data
    df = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'], 'B': ['>0.12<', '>3.45<', '>6.78<']})
    df.iloc[0, 0] = 'invalid_data'
    expected_df = pd.DataFrame({'A': [np.nan, 4.56, 7.89], 'B': [0.12, 3.45, 6.78]})
    result_df = task_func(df)
    assert result_df.equals(expected_df)

    # Test case 3: Test with a dataframe with no data
    df = pd.DataFrame({'A': [], 'B': []})
    expected_df = pd.DataFrame({'A': [], 'B': []})
    result_df = task_func(df)
    assert result_df.equals(expected_df)

    # Test case 4: Test with a dataframe with NaN data
    df = pd.DataFrame({'A': [np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, np.nan]})
    expected_df = pd.DataFrame({'A': [np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, np.nan]})
    result_df = task_func(df)
    assert result_df.equals(expected_df)