import pytest
from src_0115 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_with_valid_input():
    input_dict = {'array': np.array([1, 2, 3, 4, 5])}
    expected_output = {'array': np.array([1, 2, 3, 4, 5]), 'normalized_array': np.array([0., 0.25, 0.5, 0.75, 1.])}
    assert task_func(input_dict) == expected_output

def test_task_func_with_invalid_input_type():
    input_dict = {'array': [1, 2, 3, 4, 5]}
    with pytest.raises(TypeError):
        task_func(input_dict)

def test_task_func_with_empty_array():
    input_dict = {'array': np.array([])}
    expected_output = {'array': np.array([]), 'normalized_array': np.array([])}
    assert task_func(input_dict) == expected_output

def test_task_func_with_single_element_array():
    input_dict = {'array': np.array([10])}
    expected_output = {'array': np.array([10]), 'normalized_array': np.array([0.])}
    assert task_func(input_dict) == expected_output

def test_task_func_with_negative_values():
    input_dict = {'array': np.array([-1, -2, -3, -4, -5])}
    expected_output = {'array': np.array([-1, -2, -3, -4, -5]), 'normalized_array': np.array([1., 0.75, 0.5, 0.25, 0.])}
    assert task_func(input_dict) == expected_output

def test_task_func_with_mixed_positive_and_negative_values():
    input_dict = {'array': np.array([-1, 0, 1])}
    expected_output = {'array': np.array([-1, 0, 1]), 'normalized_array': np.array([0., 0.5, 1.])}
    assert task_func(input_dict) == expected_output