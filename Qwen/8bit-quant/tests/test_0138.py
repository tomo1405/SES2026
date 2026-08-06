import numpy as np
import pandas as pd
import pytest
from src_0138 import task_func


def test_task_func_with_valid_dataframe():
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert np.isclose(task_func(df), expected_skewness)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Input must be a non-empty pandas DataFrame."):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError, match="Input must be a non-empty pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_with_dataframe_having_all_nan_values_in_last_column():
    data = {'A': [1, 2, 3], 'B': [np.nan, np.nan, np.nan]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())  # This will be NaN because there are no non-NaN values
    assert np.isnan(task_func(df))

def test_task_func_with_dataframe_having_some_nan_values_in_last_column():
    data = {'A': [1, 2, 3], 'B': [1, np.nan, 3]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert np.isclose(task_func(df), expected_skewness)