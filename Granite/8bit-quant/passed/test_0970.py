import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0970 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

def test_task_func_with_numeric_data(input_df):
    output_df = task_func(input_df)
    assert isinstance(output_df, pd.DataFrame)
    assert output_df.shape == (3, 3)
    assert output_df.columns.tolist() == ['A', 'B', 'C']

def test_task_func_with_non_numeric_data(input_df):
    input_df['D'] = ['a', 'b', 'c']
    with pytest.raises(TypeError):
        task_func(input_df)

def test_task_func_with_empty_data(input_df):
    input_df.drop(input_df.index, inplace=True)
    with pytest.raises(ValueError):
        task_func(input_df)

def test_task_func_with_nan_values(input_df):
    input_df.loc[0, 'A'] = np.nan
    with pytest.raises(ValueError):
        task_func(input_df)