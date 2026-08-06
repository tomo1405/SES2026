import pytest
from src_0791 import task_func
import pandas as pd
import numpy as np

def test_task_func_basic():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert len(result) == 10  # Since N=10 and there are only 5 elements, it should return all indices
    assert sorted(result) == list(range(5))  # Indices of elements with the largest differences

def test_task_func_with_N_less_than_elements():
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2', N=3)
    assert len(result) == 3
    assert sorted(result) == [0, 1, 4]  # Indices of elements with the largest differences

def test_task_func_with_identical_values():
    data = {
        'col1': [1, 1, 1, 1, 1],
        'col2': [1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert len(result) == 10  # Since N=10 and there are only 5 elements, it should return all indices
    assert sorted(result) == list(range(5))  # All indices have zero difference

def test_task_func_with_missing_column():
    data = {
        'col1': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'col1', 'col2')
    assert "Columns col1 or col2 not found in the DataFrame." in str(excinfo.value)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df, 'col1', 'col2')
    assert "Columns col1 or col2 not found in the DataFrame." in str(excinfo.value)

def test_task_func_with_all_nan_values():
    data = {
        'col1': [np.nan, np.nan, np.nan, np.nan, np.nan],
        'col2': [np.nan, np.nan, np.nan, np.nan, np.nan]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'col1', 'col2')
    assert len(result) == 10  # Since N=10 and there are only 5 elements, it should return all indices
    assert sorted(result) == list(range(5))  # All indices have zero difference after scaling