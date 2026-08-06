import pandas as pd
import pytest
from statsmodels.tsa.stattools import adfuller

def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter rows based on column_b and column_c
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]

    if filtered_df[column_a].nunique() <= 1:
        return True

    # If dataframe is empty after filtering, return False
    if filtered_df.empty:
        return True

    # Perform Augmented Dickey-Fuller test
    adf_result = adfuller(filtered_df[column_a])
    p_value = adf_result[1]
    return p_value <= 0.05

def test_task_func():
    # Test case 1: nunique() <= 1
    df = pd.DataFrame({'a': [1, 1, 1], 'b': [51, 52, 53], 'c': [900, 900, 900]})
    assert task_func(df, 'a', 'b', 'c') == True

    # Test case 2: filtered_df.empty
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [51, 52, 53], 'c': [900, 900, 900]})
    assert task_func(df, 'a', 'b', 'c') == False

    # Test case 3: p_value > 0.05
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [51, 52, 53], 'c': [900, 900, 900]})
    assert task_func(df, 'a', 'b', 'c') == True