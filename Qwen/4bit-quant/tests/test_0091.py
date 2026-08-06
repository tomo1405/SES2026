import pytest
from src_0091 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_input():
    # Create sample data
    data = pd.DataFrame({
        'latitude': [40.7128, 34.0522, 37.7749],
        'longitude': [-74.0060, -118.2437, -122.4194]
    })
    target = (40.7128, -74.0060)
    k = 2

    # Expected result based on the Haversine formula calculation
    expected_result = [
        [40.7128, -74.0060],  # The target itself
        [34.0522, -118.2437]  # Closest neighbor
    ]

    # Call the function
    result = task_func(data, target, k)

    # Assert the result
    assert result == expected_result

def test_task_func_with_k_zero():
    # Create sample data
    data = pd.DataFrame({
        'latitude': [40.7128, 34.0522, 37.7749],
        'longitude': [-74.0060, -118.2437, -122.4194]
    })
    target = (40.7128, -74.0060)
    k = 0

    # Expected result is an empty list when k is 0
    expected_result = []

    # Call the function
    result = task_func(data, target, k)

    # Assert the result
    assert result == expected_result

def test_task_func_with_large_k():
    # Create sample data
    data = pd.DataFrame({
        'latitude': [40.7128, 34.0522, 37.7749],
        'longitude': [-74.0060, -118.2437, -122.4194]
    })
    target = (40.7128, -74.0060)
    k = 5  # Larger than the number of data points

    # Expected result includes all data points
    expected_result = [
        [40.7128, -74.0060],
        [34.0522, -118.2437],
        [37.7749, -122.4194]
    ]

    # Call the function
    result = task_func(data, target, k)

    # Assert the result
    assert result == expected_result

def test_task_func_with_negative_k():
    # Create sample data
    data = pd.DataFrame({
        'latitude': [40.7128, 34.0522, 37.7749],
        'longitude': [-74.0060, -118.2437, -122.4194]
    })
    target = (40.7128, -74.0060)
    k = -1

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="'k' must be a non-negative integer"):
        task_func(data, target, k)

def test_task_func_with_non_integer_k():
    # Create sample data
    data = pd.DataFrame({
        'latitude': [40.7128, 34.0522, 37.7749],
        'longitude': [-74.0060, -118.2437, -122.4194]
    })
    target = (40.7128, -74.0060)
    k = 2.5  # Non-integer value

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="'k' must be a non-negative integer"):
        task_func(data, target, k)