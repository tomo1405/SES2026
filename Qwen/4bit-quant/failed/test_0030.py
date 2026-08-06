import pytest
from src_0030 import task_func
import numpy as np
import base64

def test_task_func_with_valid_data():
    # Test with a simple 2D array
    data = np.array([[1, 2], [3, 4]])
    expected_mean = np.mean(data, axis=0)
    expected_std = np.std(data, axis=0)
    expected_standardized_data = (data - expected_mean) / expected_std
    expected_standardized_data_str = np.array2string(expected_standardized_data)
    expected_encoded_data = base64.b64encode(expected_standardized_data_str.encode('ascii')).decode('ascii')
    
    assert task_func(data) == expected_encoded_data

def test_task_func_with_single_element():
    # Test with a single element array
    data = np.array([[5]])
    expected_standardized_data = np.array([[0.]])
    expected_standardized_data_str = np.array2string(expected_standardized_data)
    expected_encoded_data = base64.b64encode(expected_standardized_data_str.encode('ascii')).decode('ascii')
    
    assert task_func(data) == expected_encoded_data

def test_task_func_with_empty_array():
    # Test with an empty array
    data = np.array([])
    expected_encoded_data = base64.b64encode(np.array2string(np.array([])).encode('ascii')).decode('ascii')
    
    assert task_func(data) == expected_encoded_data

def test_task_func_with_non_numeric_data():
    # Test with non-numeric data should raise ValueError
    data = np.array([['a', 'b'], ['c', 'd']])
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_one_dimensional_data():
    # Test with one-dimensional data
    data = np.array([1, 2, 3, 4])
    expected_mean = np.mean(data)
    expected_std = np.std(data)
    expected_standardized_data = (data - expected_mean) / expected_std
    expected_standardized_data_str = np.array2string(expected_standardized_data)
    expected_encoded_data = base64.b64encode(expected_standardized_data_str.encode('ascii')).decode('ascii')
    
    assert task_func(data) == expected_encoded_data