import pytest
from src_0904 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_with_valid_data():
    data = {
        'x1': [1, 2, 3, 4],
        'x2': [5, 6, 7, 8],
        'z': [9, 10, 11, 12]
    }
    model = task_func(data)
    assert isinstance(model, LinearRegression)

def test_task_func_with_single_predictor():
    data = {
        'x1': [1, 2, 3, 4],
        'z': [9, 10, 11, 12]
    }
    model = task_func(data)
    assert isinstance(model, LinearRegression)

def test_task_func_with_no_predictors():
    with pytest.raises(ValueError):
        data = {
            'z': [9, 10, 11, 12]
        }
        task_func(data)

def test_task_func_with_non_numeric_target():
    with pytest.raises(ValueError):
        data = {
            'x1': [1, 2, 3, 4],
            'z': ['a', 'b', 'c', 'd']
        }
        task_func(data)

def test_task_func_with_empty_data():
    with pytest.raises(ValueError):
        data = {}
        task_func(data)