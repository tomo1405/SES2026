import pytest
from src_0224 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], {})

def test_task_func_replace_values():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    dct = {'a': 1, 'b': 2}
    expected_df = pd.DataFrame({'A': [1, 2, 'c'], 'B': [1, 2, 3]})
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_encode_categorical():
    df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': [1, 2, 3]})
    dct = {}
    expected_df = pd.DataFrame({'A': [0, 1, 0], 'B': [1, 2, 3]})
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_standardize_numerical():
    df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': [1, 2, 3]})
    dct = {}
    expected_df = pd.DataFrame({
        'A': [0, 1, 0],
        'B': [(1 - 2) / 1, (2 - 2) / 1, (3 - 2) / 1]
    })
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_custom_columns():
    df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': [1, 2, 3]})
    dct = {}
    columns = ['A']
    expected_df = pd.DataFrame({
        'A': [0, 1, 0],
        'B': [1, 2, 3]
    })
    result_df = task_func(df, dct, columns=columns)
    assert result_df.equals(expected_df)