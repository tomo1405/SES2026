import pytest
from src_0152 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Test cases for the task_func function

def test_task_func():
    # Test case 1: Normal case with valid input
    data_dict = {
        'key1': [1, 2, 3],
        'key2': [4, 5, 6],
        'key3': [7, 8, 9]
    }
    data_keys = ['key1', 'key2']
    expected_output = (pd.DataFrame({
        'key1': [0.0, 0.5, 1.0],
        'key2': [0.0, 0.5, 1.0]
    }), None
    assert task_func(data_dict, data_keys) == expected_output

    # Add more test cases as needed

# Add more test cases as needed