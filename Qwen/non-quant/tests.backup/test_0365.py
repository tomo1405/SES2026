import pytest
from src_0365 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_input_type():
    with pytest.raises(ValueError, match="The input df is not a DataFrame"):
        task_func([1, 2, 3])

def test_task_func_columns():
    data = {
        'feature 1': [1, 2, 3],
        'feature 2': [4, 5, 6],
        'feature 3': [7, 8, 9],
        'feature 4': [10, 11, 12],
        'feature 5': [13, 14, 15],
        'feature 6': [16, 17, 18],
        'feature 7': [19, 20, 21],
        'feature 8': [22, 23, 24],
        'feature 9': [25, 26, 27],
        'feature 10': [28, 29, 30],
        'target': [31, 32, 33]
    }
    df = pd.DataFrame(data)
    model = task_func(df)
    assert isinstance(model, LinearRegression)

def test_task_func_missing_features():
    data = {
        'feature 1': [1, 2, 3],
        'feature 2': [4, 5, 6],
        'feature 3': [7, 8, 9],
        'feature 4': [10, 11, 12],
        'feature 5': [13, 14, 15],
        'feature 6': [16, 17, 18],
        'feature 7': [19, 20, 21],
        'feature 8': [22, 23, 24],
        'feature 9': [25, 26, 27],
        'target': [31, 32, 33]
    }
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        task_func(df)

def test_task_func_missing_target():
    data = {
        'feature 1': [1, 2, 3],
        'feature 2': [4, 5, 6],
        'feature 3': [7, 8, 9],
        'feature 4': [10, 11, 12],
        'feature 5': [13, 14, 15],
        'feature 6': [16, 17, 18],
        'feature 7': [19, 20, 21],
        'feature 8': [22, 23, 24],
        'feature 9': [25, 26, 27],
        'feature 10': [28, 29, 30]
    }
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        task_func(df)