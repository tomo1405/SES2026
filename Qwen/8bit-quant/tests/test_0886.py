import numpy as np
import pandas as pd
from src_0886 import task_func


def test_task_func_invalid_input_empty_df():
    df = pd.DataFrame()
    result = task_func(df)
    assert result is None

def test_task_func_invalid_input_missing_columns():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    result = task_func(df)
    assert result is None

def test_task_func_non_numeric_data():
    df = pd.DataFrame({'A': ['a', 'b'], 'B': [50, 51], 'C': [900, 901]})
    result = task_func(df)
    assert result is None

def test_task_func_no_data_selected():
    df = pd.DataFrame({'A': [1, 2], 'B': [49, 50], 'C': [899, 901]})
    result = task_func(df)
    assert result is None

def test_task_func_valid_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df, seed=42)
    assert isinstance(predictions, np.ndarray)
    assert isinstance(model, LinearRegression)

def test_task_func_with_seed():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions1, _ = task_func(df, seed=42)
    predictions2, _ = task_func(df, seed=42)
    np.testing.assert_array_equal(predictions1, predictions2)