import pytest
from src_0904 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_with_valid_data():
    data = {
        'x1': [1, 2, 3, 4, 5],
        'x2': [5, 4, 3, 2, 1],
        'z': [10, 11, 12, 13, 14]
    }
    df = pd.DataFrame(data)
    model = task_func(df)
    assert isinstance(model, LinearRegression)

def test_task_func_with_single_predictor():
    data = {
        'x1': [1, 2, 3, 4, 5],
        'z': [10, 11, 12, 13, 14]
    }
    df = pd.DataFrame(data)
    model = task_func(df)
    assert isinstance(model, LinearRegression)

def test_task_func_with_no_predictors():
    data = {
        'z': [10, 11, 12, 13, 14]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_with_non_numeric_target():
    data = {
        'x1': [1, 2, 3, 4, 5],
        'z': ['a', 'b', 'c', 'd', 'e']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)