import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Sample data and columns to normalize
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    columns_to_normalize = ['A', 'B']

    # Expected output after normalization
    df = pd.DataFrame(data)
    scaler = MinMaxScaler()
    expected_output = df.copy()
    expected_output[columns_to_normalize] = scaler.fit_transform(expected_output[columns_to_normalize])

    # Actual output from the function
    actual_output = task_func(data, columns_to_normalize)

    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_task_func_no_columns():
    # Test case where no columns are provided for normalization
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    columns_to_normalize = []

    # Expected output should be the same as input since no columns are normalized
    df = pd.DataFrame(data)
    expected_output = df.copy()

    # Actual output from the function
    actual_output = task_func(data, columns_to_normalize)

    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_task_func_invalid_columns():
    # Test case with invalid column names
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    columns_to_normalize = ['X', 'Y']

    # Expected output should raise a KeyError since 'X' and 'Y' are not in the DataFrame
    with pytest.raises(KeyError):
        task_func(data, columns_to_normalize)

def test_task_func_single_column():
    # Test case with a single column to normalize
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    columns_to_normalize = ['A']

    # Expected output after normalizing only column 'A'
    df = pd.DataFrame(data)
    scaler = MinMaxScaler()
    expected_output = df.copy()
    expected_output[columns_to_normalize] = scaler.fit_transform(expected_output[columns_to_normalize])

    # Actual output from the function
    actual_output = task_func(data, columns_to_normalize)

    # Check if the actual output matches the expected output
    pd.testing.assert_frame_equal(actual_output, expected_output)