import pytest
from src_0878 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(data, n_components=2)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)

def test_task_func_with_non_dataframe_input():
    data = [1, 2, 3]
    with pytest.raises(ValueError, match="data should be a DataFrame."):
        task_func(data)

def test_task_func_with_non_numeric_data():
    data = pd.DataFrame({
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data)

def test_task_func_with_n_components_greater_than_columns():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="n_components should not be greater than the number of columns in data."):
        task_func(data, n_components=3)

def test_task_func_with_single_column_data():
    data = pd.DataFrame({
        'A': [1, 2, 3]
    })
    result = task_func(data, n_components=1)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 1)

def test_task_func_with_zero_variance_columns():
    data = pd.DataFrame({
        'A': [1, 1, 1],
        'B': [2, 2, 2]
    })
    result = task_func(data, n_components=2)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
    assert np.allclose(result.iloc[:, 0], 0) and np.allclose(result.iloc[:, 1], 0)