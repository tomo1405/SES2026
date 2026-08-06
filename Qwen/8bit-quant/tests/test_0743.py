import pytest
from src_0743 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_input():
    with pytest.raises(Exception) as excinfo:
        task_func([])
    assert str(excinfo.value) == 'The input array should not be empty.'

def test_task_func_non_numeric_values():
    with pytest.raises(ValueError) as excinfo:
        task_func([('A', 'not_a_number'), ('B', 'also_not_a_number')])
    assert str(excinfo.value) == 'The values have to be numeric.'

def test_task_func_valid_input():
    input_data = [('A', 10), ('B', 20), ('C', 30)]
    expected_output = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'Value': [0.0, 0.5, 1.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_single_value():
    input_data = [('A', 10)]
    expected_output = pd.DataFrame({
        'Category': ['A'],
        'Value': [0.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_negative_values():
    input_data = [('A', -10), ('B', -20), ('C', -30)]
    expected_output = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'Value': [1.0, 0.5, 0.0]
    })
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)