import pytest
from src_0091 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_k():
    data = pd.DataFrame([[40.7128, -74.0060], [34.0522, -118.2437]], columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    with pytest.raises(ValueError, match="'k' must be a non-negative integer"):
        task_func(data, target, -1)

def test_task_func_zero_k():
    data = pd.DataFrame([[40.7128, -74.0060], [34.0522, -118.2437]], columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    result = task_func(data, target, 0)
    assert result == []

def test_task_func_k_greater_than_data_length():
    data = pd.DataFrame([[40.7128, -74.0060], [34.0522, -118.2437]], columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    result = task_func(data, target, 5)
    assert len(result) == len(data)

def test_task_func_valid_input():
    data = pd.DataFrame([[40.7128, -74.0060], [34.0522, -118.2437]], columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    result = task_func(data, target, 1)
    assert len(result) == 1
    assert result[0] == [40.7128, -74.0060]

def test_task_func_all_same_distances():
    data = pd.DataFrame([[40.7128, -74.0060], [40.7128, -74.0060]], columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    result = task_func(data, target, 2)
    assert len(result) == 2
    assert result == [[40.7128, -74.0060], [40.7128, -74.0060]]

def test_task_func_large_dataset():
    data = pd.DataFrame(np.random.rand(100, 2) * 180 - 90, columns=['latitude', 'longitude'])
    target = [40.7128, -74.0060]
    result = task_func(data, target, 5)
    assert len(result) == 5