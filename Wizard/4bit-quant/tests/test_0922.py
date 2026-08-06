python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0922 import task_func

def test_task_func():
    # Test case 1: Normal case
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 2: Empty DataFrame
    data = {}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [], 'B': []})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 3: Non-numeric columns
    data = {'A': [1, 2, 3], 'B': ['4', '5', '6']}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': ['4', '5', '6']})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 4: Non-existent columns
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    columns = ['A', 'C']
    expected_result = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [4, 5, 6]})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 5: All columns are non-numeric
    data = {'A': [1, 2, 3], 'B': ['4', '5', '6']}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': ['4', '5', '6']})
    result = task_func(data, columns)
    assert result.equals(expected_result)

    # Test case 6: All columns are empty
    data = {'A': [], 'B': []}
    columns = ['A', 'B']
    expected_result = pd.DataFrame({'A': [], 'B': []})
    result = task_func(data, columns)
    assert result.equals(expected_result)