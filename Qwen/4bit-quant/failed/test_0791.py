import pytest
from src_0791 import task_func
import pandas as pd
import numpy as np

def test_task_func_columns_exist():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Columns C or D not found in the DataFrame."):
        task_func(df, 'C', 'D')

def test_task_func_standardization():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B')
    assert np.allclose(df['A'].mean(), 0) and np.allclose(df['A'].std(), 1)
    assert np.allclose(df['B'].mean(), 0) and np.allclose(df['B'].std(), 1)

def test_task_func_largest_diff_indices():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B', N=3)
    expected = [0, 4, 1]
    assert result == expected

def test_task_func_default_N():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B')
    assert len(result) == 10

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['A', 'B'])
    with pytest.raises(ValueError, match="Columns A or B not found in the DataFrame."):
        task_func(df, 'A', 'B')