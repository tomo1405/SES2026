import pytest
from src_0902 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_input():
    result = task_func([])
    expected_columns = ['x', 'y', 'z']
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == expected_columns
    assert result.empty

def test_task_func_single_row():
    input_data = [{'x': 1, 'y': 2, 'z': 3}]
    result = task_func(input_data)
    expected_columns = ['x', 'y', 'z']
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == expected_columns
    assert not result.empty
    assert result.shape == (1, 3)

def test_task_func_multiple_rows():
    input_data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9}
    ]
    result = task_func(input_data)
    expected_columns = ['x', 'y', 'z']
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == expected_columns
    assert not result.empty
    assert result.shape == (3, 3)

def test_task_func_scaling():
    input_data = [
        {'x': 10, 'y': 20, 'z': 30},
        {'x': 40, 'y': 50, 'z': 60},
        {'x': 70, 'y': 80, 'z': 90}
    ]
    result = task_func(input_data)
    scaler = MinMaxScaler()
    expected_scaled_data = scaler.fit_transform(pd.DataFrame(input_data)[['x', 'y', 'z']])
    expected_result = pd.DataFrame(expected_scaled_data, columns=['x', 'y', 'z'])
    assert result.equals(expected_result)