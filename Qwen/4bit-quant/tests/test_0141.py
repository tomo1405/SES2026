import pytest
from src_0141 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_input_type():
    with pytest.raises(ValueError, match="The input df must be a pandas DataFrame."):
        task_func([1, 2, 3], ['col1'])

def test_task_func_cols_type():
    with pytest.raises(ValueError, match="cols must be a list of column names."):
        task_func(pd.DataFrame(), 'col1')
    with pytest.raises(ValueError, match="cols must be a list of column names."):
        task_func(pd.DataFrame(), [1, 2, 3])

def test_task_func_cols_existence():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    with pytest.raises(ValueError, match="All columns in cols must exist in the dataframe."):
        task_func(df, ['col2'])

def test_task_func_scaling():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    scaled_df = task_func(df.copy(), ['col1', 'col2'])
    scaler = StandardScaler()
    expected_scaled_values = scaler.fit_transform(df[['col1', 'col2']])
    assert scaled_df[['col1', 'col2']].equals(pd.DataFrame(expected_scaled_values, columns=['col1', 'col2']))

def test_task_func_no_change():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    result_df = task_func(df.copy(), [])
    assert result_df.equals(df)

def test_task_func_single_column():
    df = pd.DataFrame({'col1': [1, 2, 3]})
    scaled_df = task_func(df.copy(), ['col1'])
    scaler = StandardScaler()
    expected_scaled_values = scaler.fit_transform(df[['col1']])
    assert scaled_df[['col1']].equals(pd.DataFrame(expected_scaled_values, columns=['col1']))