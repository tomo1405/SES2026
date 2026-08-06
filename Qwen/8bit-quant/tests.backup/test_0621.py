import pytest
from src_0621 import task_func

def test_task_func():
    # Test with a simple input
    input_data = [[2, 3], [4, 5]]
    df = task_func(input_data)
    
    # Check if the DataFrame has the correct shape
    expected_rows = input_data[0][0] * input_data[0][1]
    expected_columns = input_data[1][0] * input_data[1][1]
    assert df.shape == (expected_rows, expected_columns), f"Expected shape {expected_rows}, {expected_columns}, but got {df.shape}"
    
    # Check if all values in the DataFrame are within the specified range
    assert df.values.min() >= RANGE[0], f"Minimum value {df.values.min()} is less than {RANGE[0]}"
    assert df.values.max() <= RANGE[1], f"Maximum value {df.values.max()} is greater than {RANGE[1]}"

def test_task_func_with_zero_dimensions():
    # Test with zero dimensions
    input_data = [[0, 0], [0, 0]]
    df = task_func(input_data)
    
    # Check if the DataFrame is empty
    assert df.empty, "Expected an empty DataFrame"
    assert df.shape == (0, 0), f"Expected shape (0, 0), but got {df.shape}"

def test_task_func_with_single_element():
    # Test with single element dimensions
    input_data = [[1, 1], [1, 1]]
    df = task_func(input_data)
    
    # Check if the DataFrame has the correct shape
    expected_rows = input_data[0][0] * input_data[0][1]
    expected_columns = input_data[1][0] * input_data[1][1]
    assert df.shape == (expected_rows, expected_columns), f"Expected shape {expected_rows}, {expected_columns}, but got {df.shape}"
    
    # Check if the value is within the specified range
    assert df.values.min() >= RANGE[0], f"Minimum value {df.values.min()} is less than {RANGE[0]}"
    assert df.values.max() <= RANGE[1], f"Maximum value {df.values.max()} is greater than {RANGE[1]}"