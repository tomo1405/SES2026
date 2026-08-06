import pytest
from src_0250 import task_func
import pandas as pd
import numpy as np

def test_task_func_default():
    train_data, test_data = task_func()
    
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    
    assert len(train_data) + len(test_data) == 10000
    assert len(train_data) == 8000
    assert len(test_data) == 2000
    
    assert all(train_data['Value'].between(0.0, 10.0))
    assert all(test_data['Value'].between(0.0, 10.0))

def test_task_func_custom_params():
    train_data, test_data = task_func(n_data_points=5000, min_value=-5.0, max_value=5.0, test_size=0.3)
    
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    
    assert len(train_data) + len(test_data) == 5000
    assert len(train_data) == 3500
    assert len(test_data) == 1500
    
    assert all(train_data['Value'].between(-5.0, 5.0))
    assert all(test_data['Value'].between(-5.0, 5.0))

def test_task_func_randomness():
    train_data1, _ = task_func(n_data_points=100, random_state=42)
    train_data2, _ = task_func(n_data_points=100, random_state=42)
    
    assert train_data1.equals(train_data2)

def test_task_func_no_data():
    with pytest.raises(ValueError):
        task_func(n_data_points=0)

def test_task_func_negative_test_size():
    with pytest.raises(ValueError):
        task_func(test_size=-0.1)

def test_task_func_invalid_test_size():
    with pytest.raises(ValueError):
        task_func(test_size=1.1)