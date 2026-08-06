import pytest
from src_0250 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func_default_values():
    train_data, test_data = task_func()
    
    # Check if the total number of data points is correct
    assert len(train_data) + len(test_data) == 10000
    
    # Check if the data is split correctly based on the default test_size (0.2)
    assert len(test_data) == pytest.approx(2000, rel=1e-2)
    
    # Check if the data is within the specified range
    assert all(min_value <= value <= max_value for value in train_data['Value'])
    assert all(min_value <= value <= max_value for value in test_data['Value'])

def test_task_func_custom_values():
    n_data_points = 5000
    min_value = 1.0
    max_value = 5.0
    test_size = 0.3
    
    train_data, test_data = task_func(n_data_points, min_value, max_value, test_size)
    
    # Check if the total number of data points is correct
    assert len(train_data) + len(test_data) == n_data_points
    
    # Check if the data is split correctly based on the custom test_size (0.3)
    assert len(test_data) == pytest.approx(1500, rel=1e-2)
    
    # Check if the data is within the specified range
    assert all(min_value <= value <= max_value for value in train_data['Value'])
    assert all(min_value <= value <= max_value for value in test_data['Value'])

def test_task_func_edge_cases():
    # Test with minimum number of data points
    train_data, test_data = task_func(n_data_points=10)
    
    # Check if the total number of data points is correct
    assert len(train_data) + len(test_data) == 10
    
    # Test with maximum number of data points
    train_data, test_data = task_func(n_data_points=100000)
    
    # Check if the total number of data points is correct
    assert len(train_data) + len(test_data) == 100000

def test_task_func_data_types():
    train_data, test_data = task_func()
    
    # Check if the returned values are DataFrames
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    
    # Check if the DataFrame has the correct column name
    assert 'Value' in train_data.columns
    assert 'Value' in test_data.columns