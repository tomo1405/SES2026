import pytest
from src_0229 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    df = pd.DataFrame(np.random.rand(5, 5), columns=['column1', 'column2', 'column3', 'column4', 'column5'])
    dct = {'a': 1, 'b': 2}
    
    with pytest.raises(ValueError):
        task_func([1, 2, 3], dct)

def test_task_func_column_names():
    data = {
        'column1': [1, 2, 3],
        'column2': [4, 5, 6],
        'column3': [7, 8, 9],
        'column4': [10, 11, 12],
        'column5': [13, 14, 15]
    }
    df = pd.DataFrame(data)
    dct = {'a': 1, 'b': 2}
    
    result = task_func(df, dct)
    assert list(result.columns) == COLUMNS
    assert list(result.index) == COLUMNS

def test_task_func_correlation_matrix():
    data = {
        'column1': [1, 2, 3],
        'column2': [4, 5, 6],
        'column3': [7, 8, 9],
        'column4': [10, 11, 12],
        'column5': [13, 14, 15]
    }
    df = pd.DataFrame(data)
    dct = {'a': 1, 'b': 2}
    
    result = task_func(df, dct)
    expected_corr_matrix = np.corrcoef(df.values, rowvar=False)
    assert np.array_equal(result.values, expected_corr_matrix)

def test_task_func_replace_values():
    data = {
        'column1': ['a', 'b', 'c'],
        'column2': ['d', 'e', 'f'],
        'column3': ['g', 'h', 'i'],
        'column4': ['j', 'k', 'l'],
        'column5': ['m', 'n', 'o']
    }
    df = pd.DataFrame(data)
    dct = {'a': 1, 'b': 2, 'c': 3}
    
    result = task_func(df, dct)
    expected_df = df.replace(dct)
    expected_corr_matrix = np.corrcoef(expected_df.values, rowvar=False)
    assert np.array_equal(result.values, expected_corr_matrix)