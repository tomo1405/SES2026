import pytest
from src_0747 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_df_type():
    with pytest.raises(ValueError, match="df should be a DataFrame."):
        task_func([1, 2, 3], 'target')

def test_task_func_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="df should contain at least one row"):
        task_func(df, 'target')

def test_task_func_missing_target_column():
    df = pd.DataFrame({'feature': [1, 2, 3]})
    with pytest.raises(ValueError, match="target_column should be in DataFrame"):
        task_func(df, 'target')

def test_task_func_non_numeric_values():
    df = pd.DataFrame({'feature': ['a', 'b', 'c'], 'target': [1, 2, 3]})
    with pytest.raises(ValueError, match="df values should be numeric only"):
        task_func(df, 'target')

def test_task_func_valid_input():
    df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    model = task_func(df, 'target')
    assert isinstance(model, LinearRegression)

def test_task_func_with_target_values():
    df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    target_values = [7, 8]
    model = task_func(df, 'target', target_values=target_values)
    assert isinstance(model, LinearRegression)

def test_task_func_with_no_target_values():
    df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    model = task_func(df, 'target')
    assert isinstance(model, LinearRegression)