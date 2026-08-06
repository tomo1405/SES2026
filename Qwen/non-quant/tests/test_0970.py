import pytest
from src_0970 import task_func
import pandas as pd
import numpy as np

def test_task_func_numeric_data():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    expected_output = pd.DataFrame({
        'A': [0.0, 0.333333, 0.666667],
        'B': [0.0, 0.333333, 0.666667]
    })
    result = task_func(df)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_non_numeric_data():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    with pytest.raises(TypeError):
        task_func(df)

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_dataframe_with_nan():
    df = pd.DataFrame({
        'A': [1, 2, np.nan],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_single_row_dataframe():
    df = pd.DataFrame({
        'A': [1],
        'B': [4]
    })
    expected_output = pd.DataFrame({
        'A': [0.0],
        'B': [0.0]
    })
    result = task_func(df)
    pd.testing.assert_frame_equal(result, expected_output)