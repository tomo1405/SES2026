import pytest
from src_0138 import task_func
import pandas as pd
from scipy.stats import skew

def test_task_func_with_valid_dataframe():
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert task_func(df) == expected_skewness

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == "Input must be a non-empty pandas DataFrame."

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError) as excinfo:
        task_func([1, 2, 3])
    assert str(excinfo.value) == "Input must be a non-empty pandas DataFrame."

def test_task_func_with_dataframe_having_nan_values():
    data = {'A': [1, 2, None, 4, 5], 'B': [None, 4, 3, 2, 1]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert task_func(df) == expected_skewness

def test_task_func_with_single_column_dataframe():
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['A'].dropna())
    assert task_func(df) == expected_skewness