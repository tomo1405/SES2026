import pytest
from src_0970 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_numeric_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0]
    }))

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Input DataFrame is empty or contains NaN values."):
        task_func(df)

def test_task_func_with_non_numeric_data():
    data = {
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    with pytest.raises(TypeError, match="Input DataFrame contains non-numeric data types."):
        task_func(df)

def test_task_func_with_nan_values():
    data = {
        'A': [1, 2, np.nan],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Input DataFrame is empty or contains NaN values."):
        task_func(df)

def test_task_func_with_single_row():
    data = {
        'A': [1],
        'B': [2]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({
        'A': [0.0],
        'B': [0.0]
    }))

def test_task_func_with_single_column():
    data = {
        'A': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({
        'A': [0.0, 0.5, 1.0]
    }))