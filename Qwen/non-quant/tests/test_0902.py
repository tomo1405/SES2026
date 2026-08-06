import pytest
from src_0902 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_input():
    result = task_func([])
    expected = pd.DataFrame(columns=['x', 'y', 'z'])
    assert result.equals(expected)

def test_task_func_single_row():
    data = [{'x': 1, 'y': 2, 'z': 3}]
    result = task_func(data)
    expected = pd.DataFrame({'x': [0.0], 'y': [0.0], 'z': [0.0]})
    assert result.equals(expected)

def test_task_func_multiple_rows():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    result = task_func(data)
    expected = pd.DataFrame({'x': [0.0, 1.0], 'y': [0.0, 1.0], 'z': [0.0, 1.0]})
    assert result.equals(expected)

def test_task_func_with_zero_range():
    data = [{'x': 1, 'y': 1, 'z': 1}, {'x': 1, 'y': 1, 'z': 1}]
    result = task_func(data)
    expected = pd.DataFrame({'x': [0.0, 0.0], 'y': [0.0, 0.0], 'z': [0.0, 0.0]})
    assert result.equals(expected)

def test_task_func_with_negative_values():
    data = [{'x': -1, 'y': -2, 'z': -3}, {'x': 1, 'y': 2, 'z': 3}]
    result = task_func(data)
    expected = pd.DataFrame({'x': [0.0, 1.0], 'y': [0.0, 1.0], 'z': [0.0, 1.0]})
    assert result.equals(expected)