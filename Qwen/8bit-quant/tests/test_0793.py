import pandas as pd
import pytest
from src_0793 import task_func


def test_task_func_basic():
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    feature = 'feature'
    target = 'target'
    indices, model = task_func(df, feature, target)
    assert len(indices) == 10
    assert all(isinstance(i, int) for i in indices)
    assert isinstance(model, LinearRegression)

def test_task_func_with_n():
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    feature = 'feature'
    target = 'target'
    n = 3
    indices, model = task_func(df, feature, target, n=n)
    assert len(indices) == n
    assert all(isinstance(i, int) for i in indices)
    assert isinstance(model, LinearRegression)

def test_task_func_missing_column():
    data = {
        'feature': [1, 2, 3, 4, 5],
        'target': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    feature = 'missing_feature'
    target = 'target'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, feature, target)
    assert str(excinfo.value) == "Columns missing_feature or target not found in the DataFrame."

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    feature = 'feature'
    target = 'target'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, feature, target)
    assert str(excinfo.value) == "Columns feature or target not found in the DataFrame."

def test_task_func_non_numeric_data():
    data = {
        'feature': ['a', 'b', 'c', 'd', 'e'],
        'target': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    feature = 'feature'
    target = 'target'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, feature, target)
    assert str(excinfo.value) == "Columns feature or target not found in the DataFrame."