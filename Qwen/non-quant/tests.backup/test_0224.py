import pytest
from src_0224 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], {})

def test_task_func_replace_values():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    dct = {'a': 1, 'b': 2}
    expected_df = pd.DataFrame({'A': [1, 2, 'c'], 'B': [1, 2, 3]})
    result_df = task_func(df, dct)
    assert result_df.equals(expected_df)

def test_task_func_label_encoding():
    df = pd.DataFrame({'A': ['cat', 'dog', 'bird'], 'B': [1, 2, 3]})
    dct = {}
    result_df = task_func(df, dct)
    assert result_df['A'].nunique() == 3  # Check if all categories are encoded

def test_task_func_standardization():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    dct = {}
    result_df = task_func(df, dct)
    assert result_df['A'].mean() == 0
    assert result_df['A'].std() == 1
    assert result_df['B'].mean() == 0
    assert result_df['B'].std() == 1

def test_task_func_specific_columns():
    df = pd.DataFrame({'A': ['cat', 'dog', 'bird'], 'B': [1, 2, 3]})
    dct = {}
    columns = ['A']
    result_df = task_func(df, dct, columns=columns)
    assert result_df['A'].nunique() == 3  # Check if only 'A' is encoded
    assert result_df['B'].nunique() == 3  # Check if 'B' remains unchanged

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    dct = {}
    result_df = task_func(df, dct)
    assert result_df.empty