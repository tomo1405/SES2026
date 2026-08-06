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
    expected_output = pd.DataFrame({
        'A': [0.0, 0.5, 1.0],
        'B': [0.0, 0.5, 1.0],
        'C': [0.0, 0.5, 1.0]
    })
    output = task_func(input_df)
    pd.testing.assert_frame_equal(output, expected_output)

def test_task_func_with_non_numeric_data(input_df):
    input_df['D'] = ['a', 'b', 'c']
    with pytest.raises(TypeError):
        task_func(input_df)

def test_task_func_with_empty_data(input_df):
    input_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(input_df)

def test_task_func_with_nan_values(input_df):
    input_df.loc[0, 'A'] = np.nan
    with pytest.raises(ValueError):
        task_func(input_df)