import pytest
from src_0706 import task_func
import pandas as pd
import numpy as np

def test_task_func_column_not_in_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'C'
    alpha = 0.05
    with pytest.raises(ValueError) as excinfo:
        task_func(df, column, alpha)
    assert str(excinfo.value) == 'Column does not exist in DataFrame'

def test_task_func_shapiro_test():
    np.random.seed(0)
    data = np.random.normal(loc=0, scale=1, size=100)
    df = pd.DataFrame({'data': data})
    column = 'data'
    alpha = 0.05
    result = task_func(df, column, alpha)
    assert isinstance(result, bool)

def test_task_func_alpha_zero():
    df = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
    column = 'data'
    alpha = 0
    result = task_func(df, column, alpha)
    assert result is True

def test_task_func_alpha_one():
    df = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
    column = 'data'
    alpha = 1
    result = task_func(df, column, alpha)
    assert result is True

def test_task_func_adjusted_data():
    df = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
    column = 'data'
    alpha = 0.05
    task_func(df, column, alpha)
    assert df[column].mean() == 0