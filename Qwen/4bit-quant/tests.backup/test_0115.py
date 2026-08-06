import pytest
from src_0115 import task_func
import numpy as np

def test_task_func_with_valid_input():
    input_data = {
        "array": np.array([1, 2, 3, 4, 5])
    }
    expected_output = {
        "array": np.array([1, 2, 3, 4, 5]),
        "normalized_array": np.array([0., 0.25, 0.5, 0.75, 1.])
    }
    result = task_func(input_data)
    assert np.allclose(result['normalized_array'], expected_output['normalized_array'])

def test_task_func_with_invalid_input_type():
    input_data = {
        "array": [1, 2, 3, 4, 5]  # Not a numpy array
    }
    with pytest.raises(TypeError):
        task_func(input_data)

def test_task_func_with_single_element_array():
    input_data = {
        "array": np.array([10])
    }
    expected_output = {
        "array": np.array([10]),
        "normalized_array": np.array([0.])
    }
    result = task_func(input_data)
    assert np.allclose(result['normalized_array'], expected_output['normalized_array'])

def test_task_func_with_empty_array():
    input_data = {
        "array": np.array([])
    }
    expected_output = {
        "array": np.array([]),
        "normalized_array": np.array([])
    }
    result = task_func(input_data)
    assert np.allclose(result['normalized_array'], expected_output['normalized_array'])