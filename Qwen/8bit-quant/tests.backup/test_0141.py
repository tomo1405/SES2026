import pytest
from src_0141 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_invalid_df_type():
    with pytest.raises(ValueError, match="The input df must be a pandas DataFrame."):
        task_func([1, 2, 3], ['col1'])

def test_task_func_invalid_cols_type():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    with pytest.raises(ValueError, match="cols must be a list of column names."):
        task_func(df, 'col1')

def test_task_func_cols_not_in_df():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    with pytest.raises(ValueError, match="All columns in cols must exist in the dataframe."):
        task_func(df, ['col2'])

def test_task_func_valid_input():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    cols = ['col1', 'col2']
    result = task_func(df, cols)
    
    # Check if the DataFrame is modified correctly
    scaler = StandardScaler()
    expected = scaler.fit_transform(df[cols])
    assert result[cols].equals(pd.DataFrame(expected, columns=cols))

def test_task_func_no_change_if_cols_empty():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    cols = []
    result = task_func(df, cols)
    
    # Check if the DataFrame remains unchanged
    assert result.equals(df)

def test_task_func_single_column():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    cols = ['col1']
    result = task_func(df, cols)
    
    # Check if the DataFrame is modified correctly for a single column
    scaler = StandardScaler()
    expected = scaler.fit_transform(df[cols])
    assert result[cols].equals(pd.DataFrame(expected, columns=cols))