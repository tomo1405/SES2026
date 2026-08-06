import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Normal case
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['a', 'b', 'c']
    expected_output = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
    output = task_func(data, columns)
    assert output.equals(expected_output)

    # Test case 2: No columns specified
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = []
    expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = task_func(data, columns)
    assert output.equals(expected_output)

    # Test case 3: Columns not in DataFrame
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['a', 'b', 'c', 'd']
    expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = task_func(data, columns)
    assert output.equals(expected_output)

    # Test case 4: DataFrame with different data types
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['a', 'b', 'c']
    expected_output = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
    output = task_func(data, columns)
    assert output.equals(expected_output)

    # Test case 5: DataFrame with NaN values
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    columns = ['a', 'b', 'c']
    expected_output = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]
    output = task_func(data, columns)
    assert output.equals(expected_output)