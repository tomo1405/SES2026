import pytest
from src_0879 import task_func
import numpy as np
import pandas as pd

def test_task_func_basic():
    # Create a simple dataset
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    mse, model, returned_data = task_func(df, 'target')
    
    # Check if the returned data is the same as the input data
    assert returned_data.equals(df), "The returned data does not match the input data."
    
    # Check if the MSE is a non-negative number
    assert mse >= 0, "Mean Squared Error should be non-negative."

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func([], 'target')

def test_task_func_missing_target():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df, 'target')

def test_task_func_random_state():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    mse1, _, _ = task_func(df, 'target', random_state=42)
    mse2, _, _ = task_func(df, 'target', random_state=42)
    
    # Check if the MSEs are the same when random_state is set
    assert mse1 == mse2, "MSEs should be the same when random_state is set."

def test_task_func_different_test_size():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    mse1, _, _ = task_func(df, 'target', test_size=0.2)
    mse2, _, _ = task_func(df, 'target', test_size=0.5)
    
    # Check if the MSEs are different when test_size is changed
    assert mse1 != mse2, "MSEs should be different when test_size is changed."