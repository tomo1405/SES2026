import pandas as pd
import pytest
from src_0879 import task_func


def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func([], 'target')

def test_task_func_missing_target():
    data = {'feature1': [1, 2, 3], 'feature2': [4, 5, 6]}
    with pytest.raises(ValueError):
        task_func(data, 'target')

def test_task_func_valid_data():
    data = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1], 'target': [10, 20, 30, 40, 50]}
    mse, model, df = task_func(data, 'target')
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_task_func_with_random_state():
    data = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1], 'target': [10, 20, 30, 40, 50]}
    mse1, _, _ = task_func(data, 'target', random_state=42)
    mse2, _, _ = task_func(data, 'target', random_state=42)
    assert mse1 == mse2

def test_task_func_with_different_test_size():
    data = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1], 'target': [10, 20, 30, 40, 50]}
    mse1, _, _ = task_func(data, 'target', test_size=0.2)
    mse2, _, _ = task_func(data, 'target', test_size=0.5)
    assert mse1 != mse2