import pytest
from src_0970 import task_func
import numpy as np
import pandas as pd

def test_task_func_input_dataframe_contains_non_numeric_data_types():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    with pytest.raises(TypeError):
        task_func(df)

def test_task_func_input_dataframe_is_empty_or_contains_nan_values():
    df = pd.DataFrame({'A': [np.nan, np.nan, np.nan], 'B': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_output_dataframe_has_correct_shape():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_norm_cumsum = task_func(df)
    assert df_norm_cumsum.shape == (3, 2)

def test_task_func_output_dataframe_has_correct_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_norm_cumsum = task_func(df)
    assert df_norm_cumsum.columns.tolist() == ['A', 'B']

def test_task_func_output_dataframe_has_correct_values():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_norm_cumsum = task_func(df)
    expected_values = [[1, 4], [2, 5], [3, 6]]
    assert np.allclose(df_norm_cumsum.values, expected_values)