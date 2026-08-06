import pytest
from src_0753 import task_func
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [1, 2, 3, 4, 5]
    })
    target_column = 'target'
    result = task_func(data=data, target_column=target_column)
    assert isinstance(result, float), "The result should be a float"

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError):
        task_func(data="invalid_data", target_column='target')

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func(data=pd.DataFrame(), target_column='target')

def test_task_func_invalid_target_column():
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [1, 2, 3, 4, 5]
    })
    with pytest.raises(ValueError):
        task_func(data=data, target_column='non_existent_column')

def test_task_func_invalid_test_size():
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [1, 2, 3, 4, 5]
    })
    with pytest.raises(ValueError):
        task_func(data=data, target_column='target', test_size=1.5)

def test_task_func_invalid_random_state():
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [1, 2, 3, 4, 5]
    })
    with pytest.raises(ValueError):
        task_func(data=data, target_column='target', random_state="invalid")