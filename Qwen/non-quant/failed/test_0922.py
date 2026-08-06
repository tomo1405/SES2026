import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test with simple data and single column
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [4, 5, 6]})
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with multiple columns
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    columns = ['A', 'B']
    expected_output = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0], 'C': [7, 8, 9]})
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with no columns to normalize
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = []
    expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with all columns to normalize
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A', 'B']
    expected_output = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with one column that has constant values
    data = {'A': [1, 1, 1], 'B': [4, 5, 6]}
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.0, 0.0, 0.0], 'B': [4, 5, 6]})
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with empty DataFrame
    data = {}
    columns = []
    expected_output = pd.DataFrame()
    result = task_func(data, columns)
    pd.testing.assert_frame_equal(result, expected_output)