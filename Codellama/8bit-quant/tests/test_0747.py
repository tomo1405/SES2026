import pytest
from src_0747 import task_func
import numpy as np
import pandas as pd

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [7, 8, 9]
    model = task_func(df, target_column, target_values)
    assert isinstance(model, LinearRegression)

def test_task_func_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'D'
    target_values = [7, 8, 9]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

def test_task_func_invalid_input_2():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [10, 11, 12]
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

def test_task_func_invalid_input_3():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = None
    with pytest.raises(ValueError):
        task_func(df, target_column, target_values)

def test_task_func_invalid_input_4():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target_column = 'C'
    target_values = [7, 8, 9]
    df = df.applymap(lambda x: x if x in target_values else 0)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    model = LinearRegression().fit(X, y)
    assert isinstance(model, LinearRegression)
    assert model.coef_[0] == 1
    assert model.intercept_ == 0