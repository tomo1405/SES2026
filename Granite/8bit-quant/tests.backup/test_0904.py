import pandas as pd
from sklearn.linear_model import LinearRegression
from src_0904 import task_func
import pytest

def test_task_func():
    d = {'x': [1, 2, 3], 'y': [2, 3, 4], 'z': [3, 4, 5]}
    model = task_func(d)
    assert isinstance(model, LinearRegression)

def test_task_func_with_custom_target():
    d = {'x': [1, 2, 3], 'y': [2, 3, 4], 'z': [3, 4, 5]}
    model = task_func(d, target='y')
    assert isinstance(model, LinearRegression)

def test_task_func_with_invalid_target():
    d = {'x': [1, 2, 3], 'y': [2, 3, 4], 'z': [3, 4, 5]}
    with pytest.raises(ValueError):
        task_func(d, target='invalid')