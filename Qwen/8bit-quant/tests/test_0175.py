import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError, match="Input 'data' must be a pandas DataFrame."):
        task_func([1, 2, 3], 'new_key', 1, 10)

def test_task_func_valid_data():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'new_key', 1, 10)
    assert 'new_key' in result.columns
    assert len(result) == len(df)
    assert result['new_key'].dtype == np.int64
    assert all(1 <= value <= 10 for value in result['new_key'])

def test_task_func_min_max_values():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'new_key', 5, 15)
    assert all(5 <= value <= 15 for value in result['new_key'])

def test_task_func_no_rows():
    df = pd.DataFrame()
    result = task_func(df, 'new_key', 1, 10)
    assert 'new_key' in result.columns
    assert len(result) == 0

def test_task_func_large_dataframe():
    df = pd.DataFrame({'A': range(1000)})
    result = task_func(df, 'new_key', 1, 100)
    assert 'new_key' in result.columns
    assert len(result) == 1000
    assert all(1 <= value <= 100 for value in result['new_key'])