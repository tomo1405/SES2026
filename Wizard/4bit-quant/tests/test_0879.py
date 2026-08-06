python
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from src_0879 import task_func


def test_task_func_valid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'A'
    mse, model, data = task_func(data, target)
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)


def test_task_func_empty_data():
    data = pd.DataFrame()
    target = 'A'
    with pytest.raises(ValueError):
        task_func(data, target)


def test_task_func_target_not_in_data():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'D'
    with pytest.raises(ValueError):
        task_func(data, target)


def test_task_func_test_size_0():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'A'
    mse, model, data = task_func(data, target, test_size=0)
    assert mse == 0.0


def test_task_func_test_size_1():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'A'
    mse, model, data = task_func(data, target, test_size=1)
    assert mse == 0.0


def test_task_func_test_size_0_5():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'A'
    mse, model, data = task_func(data, target, test_size=0.5)
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)