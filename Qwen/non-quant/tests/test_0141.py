import pytest
from src_0141 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_valid_input():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = ['A', 'B']
    result = task_func(df, cols)
    assert isinstance(result, pd.DataFrame)
    assert all(isinstance(col, str) for col in result.columns)
    assert all(col in result.columns for col in cols)
    assert (result[cols] != df[cols]).all().all(), "Data should be scaled"

def test_task_func_invalid_df_type():
    with pytest.raises(ValueError, match="The input df must be a pandas DataFrame."):
        task_func([1, 2, 3], ['A'])

def test_task_func_invalid_cols_type():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="cols must be a list of column names."):
        task_func(df, 'A')

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    cols = ['A', 'B']
    with pytest.raises(ValueError, match="All columns in cols must exist in the dataframe."):
        task_func(df, cols)

def test_task_func_no_columns_to_scale():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    cols = []
    result = task_func(df, cols)
    assert result.equals(df), "DataFrame should remain unchanged if no columns to scale"

def test_task_func_single_column():
    df = pd.DataFrame({
        'A': [1, 2, 3]
    })
    cols = ['A']
    result = task_func(df, cols)
    assert (result[cols] != df[cols]).all().all(), "Single column should be scaled"