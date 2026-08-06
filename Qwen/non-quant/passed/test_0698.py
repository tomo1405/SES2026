import pytest
from src_0698 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_positive_slope():
    df = pd.DataFrame({
        'feature': [1, 2, 3, 4, 5],
        'value': [2, 4, 6, 8, 10]
    })
    result = task_func(df)
    assert result == {'coefficients': [[2.0]], 'intercept': [0.0]}

def test_task_func_with_negative_slope():
    df = pd.DataFrame({
        'feature': [1, 2, 3, 4, 5],
        'value': [10, 8, 6, 4, 2]
    })
    result = task_func(df)
    assert result == {'coefficients': [[-2.0]], 'intercept': [12.0]}

def test_task_func_with_zero_slope():
    df = pd.DataFrame({
        'feature': [1, 2, 3, 4, 5],
        'value': [5, 5, 5, 5, 5]
    })
    result = task_func(df)
    assert result == {'coefficients': [[0.0]], 'intercept': [5.0]}

def test_task_func_single_point():
    df = pd.DataFrame({
        'feature': [1],
        'value': [2]
    })
    result = task_func(df)
    assert result == {'coefficients': [[0.0]], 'intercept': [2.0]}

def test_task_func_with_non_linear_data():
    df = pd.DataFrame({
        'feature': [1, 2, 3, 4, 5],
        'value': [1, 4, 9, 16, 25]
    })
    result = task_func(df)
    assert result['coefficients'][0][0] > 0  # Positive slope
    assert result['intercept'][0] < 0      # Negative intercept

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['feature', 'value'])
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'feature': [1, 2, 3],
        'value': [4, 5, 6]
    })
    df.drop(columns=['value'], inplace=True)
    with pytest.raises(KeyError):
        task_func(df)

    df = pd.DataFrame({
        'feature': [1, 2, 3],
        'value': [4, 5, 6]
    })
    df.drop(columns=['feature'], inplace=True)
    with pytest.raises(KeyError):
        task_func(df)