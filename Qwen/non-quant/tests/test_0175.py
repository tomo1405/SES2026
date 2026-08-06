import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], 'key', 1, 10)

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'B', 1, 10)
    assert 'B' in result.columns
    assert len(result) == len(df)
    assert all(1 <= x <= 10 for x in result['B'])

def test_task_func_min_max_values():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'C', 5, 5)
    assert all(x == 5 for x in result['C'])

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    result = task_func(df, 'D', 1, 10)
    assert 'D' in result.columns
    assert len(result) == 0

def test_task_func_large_dataframe():
    df = pd.DataFrame(np.random.rand(1000, 5))
    result = task_func(df, 'E', 1, 100)
    assert 'E' in result.columns
    assert len(result) == 1000
    assert all(1 <= x <= 100 for x in result['E'])