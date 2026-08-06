import pytest
from src_0878 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError, match="data should be a DataFrame."):
        task_func([1, 2, 3])

def test_task_func_non_numeric_values():
    data = pd.DataFrame({
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data)

def test_task_func_n_components_greater_than_columns():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="n_components should not be greater than the number of columns in data."):
        task_func(data, n_components=3)

def test_task_func_valid_input():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(data)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)

def test_task_func_single_component():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
    result = task_func(data, n_components=1)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 1)

def test_task_func_no_reduction():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(data, n_components=2)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)