import pytest
from src_0747 import task_func
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_with_valid_data():
    df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })
    target_column = 'target'
    model = task_func(df, target_column)
    assert isinstance(model, LinearRegression)

def test_task_func_with_invalid_df_type():
    with pytest.raises(ValueError, match="df should be a DataFrame."):
        task_func([1, 2, 3], 'target')

def test_task_func_with_empty_df():
    with pytest.raises(ValueError, match="df should contain at least one row"):
        task_func(pd.DataFrame(), 'target')

def test_task_func_with_missing_target_column():
    df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="target_column should be in DataFrame"):
        task_func(df, 'target')

def test_task_func_with_non_numeric_values():
    df = pd.DataFrame({
        'feature1': [1, 2, 'a'],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })
    with pytest.raises(ValueError, match="df values should be numeric only"):
        task_func(df, 'target')

def test_task_func_with_target_values():
    df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })
    target_column = 'target'
    target_values = [7, 8]
    model = task_func(df, target_column, target_values)
    assert isinstance(model, LinearRegression)
    assert (df['target'] == [7, 8, 0]).all()

def test_task_func_with_none_target_values():
    df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [7, 8, 9]
    })
    target_column = 'target'
    model = task_func(df, target_column, None)
    assert isinstance(model, LinearRegression)
    assert (df['target'] == [7, 8, 9]).all()