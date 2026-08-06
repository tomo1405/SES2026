python
import numpy as np
import pytest
from sklearn.linear_model import LinearRegression
from src_0698 import task_func

def test_task_func():
    df = {'feature': [1, 2, 3], 'value': [4, 5, 6]}
    expected_result = {'coefficients': [4.0], 'intercept': [1.0]}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_nan():
    df = {'feature': [1, 2, 3], 'value': [4, np.nan, 6]}
    expected_result = {'coefficients': [4.0], 'intercept': [1.0]}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_inf():
    df = {'feature': [1, 2, 3], 'value': [4, np.inf, 6]}
    expected_result = {'coefficients': [4.0], 'intercept': [1.0]}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_zero_division():
    df = {'feature': [1, 2, 3], 'value': [4, 0, 6]}
    expected_result = {'coefficients': [4.0], 'intercept': [1.0]}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_empty_df():
    df = {}
    expected_result = {'coefficients': [], 'intercept': []}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_single_row_df():
    df = {'feature': [1], 'value': [4]}
    expected_result = {'coefficients': [4.0], 'intercept': [1.0]}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_single_column_df():
    df = {'feature': [1, 2, 3], 'value': [4]}
    expected_result = {'coefficients': [], 'intercept': []}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_invalid_df():
    df = {'feature': [1, 2, 3], 'value': [4, 'a', 6]}
    expected_result = {'coefficients': [], 'intercept': []}
    result = task_func(df)
    assert result == expected_result