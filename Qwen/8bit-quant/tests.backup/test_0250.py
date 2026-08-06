import pytest
from src_0250 import task_func
import pandas as pd

def test_task_func_default_parameters():
    train_data, test_data = task_func()
    
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    
    assert len(train_data) + len(test_data) == 10000
    assert 'Value' in train_data.columns
    assert 'Value' in test_data.columns
    
    assert train_data['Value'].min() >= 0.0
    assert train_data['Value'].max() <= 10.0
    assert test_data['Value'].min() >= 0.0
    assert test_data['Value'].max() <= 10.0

def test_task_func_custom_parameters():
    n_data_points = 5000
    min_value = 5.0
    max_value = 15.0
    test_size = 0.3
    
    train_data, test_data = task_func(n_data_points, min_value, max_value, test_size)
    
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    
    assert len(train_data) + len(test_data) == n_data_points
    assert 'Value' in train_data.columns
    assert 'Value' in test_data.columns
    
    assert train_data['Value'].min() >= min_value
    assert train_data['Value'].max() <= max_value
    assert test_data['Value'].min() >= min_value
    assert test_data['Value'].max() <= max_value
    
    assert len(train_data) == int(n_data_points * (1 - test_size))
    assert len(test_data) == int(n_data_points * test_size)