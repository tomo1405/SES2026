import pytest
from src_0030 import task_func
import numpy as np
import base64

def test_task_func():
    # Test with a simple 2D array
    data = np.array([[1, 2], [3, 4]])
    result = task_func(data)
    
    # Decode the base64 string to compare
    decoded_result = base64.b64decode(result).decode('ascii')
    
    # Convert the decoded string back to a numpy array
    decoded_array = np.fromstring(decoded_result[1:-1], sep=' ')
    decoded_array = decoded_array.reshape((2, 2))
    
    # Calculate the expected standardized data using StandardScaler
    scaler = StandardScaler()
    expected_array = scaler.fit_transform(data)
    
    # Check if the decoded array matches the expected array
    assert np.allclose(decoded_array, expected_array)

def test_task_func_empty_input():
    # Test with an empty input
    data = np.array([])
    result = task_func(data)
    
    # Decode the base64 string to compare
    decoded_result = base64.b64decode(result).decode('ascii')
    
    # Convert the decoded string back to a numpy array
    decoded_array = np.fromstring(decoded_result[1:-1], sep=' ')
    decoded_array = decoded_array.reshape((0, 0))
    
    # Calculate the expected standardized data using StandardScaler
    scaler = StandardScaler()
    expected_array = scaler.fit_transform(data)
    
    # Check if the decoded array matches the expected array
    assert np.array_equal(decoded_array, expected_array)

def test_task_func_single_element():
    # Test with a single element input
    data = np.array([[5]])
    result = task_func(data)
    
    # Decode the base64 string to compare
    decoded_result = base64.b64decode(result).decode('ascii')
    
    # Convert the decoded string back to a numpy array
    decoded_array = np.fromstring(decoded_result[1:-1], sep=' ')
    decoded_array = decoded_array.reshape((1, 1))
    
    # Calculate the expected standardized data using StandardScaler
    scaler = StandardScaler()
    expected_array = scaler.fit_transform(data)
    
    # Check if the decoded array matches the expected array
    assert np.allclose(decoded_array, expected_array)