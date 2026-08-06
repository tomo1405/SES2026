import pytest
from src_0688 import task_func
import numpy as np
from scipy.stats import mode

def test_task_func_with_single_mode():
    input_data = [[1, 2, 2, 3], [4, 2, 5]]
    expected_output = (np.array([2]), np.array([4]))
    assert task_func(input_data) == expected_output

def test_task_func_with_multiple_modes():
    input_data = [[1, 1, 2, 2], [3, 3, 4, 4]]
    expected_output = (np.array([1, 2, 3, 4]), np.array([2, 2, 2, 2]))
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_lists():
    input_data = [[], []]
    expected_output = (np.array([]), np.array([]))
    assert task_func(input_data) == expected_output

def test_task_func_with_single_element_lists():
    input_data = [[1], [2], [3]]
    expected_output = (np.array([1, 2, 3]), np.array([1, 1, 1]))
    assert task_func(input_data) == expected_output

def test_task_func_with_negative_numbers():
    input_data = [[-1, -2, -2, -3], [-4, -2, -5]]
    expected_output = (np.array([-2]), np.array([3]))
    assert task_func(input_data) == expected_output

def test_task_func_with_floats():
    input_data = [[1.1, 2.2, 2.2, 3.3], [4.4, 2.2, 5.5]]
    expected_output = (np.array([2.2]), np.array([3]))
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_types():
    with pytest.raises(TypeError):
        input_data = [[1, 'a', 2], ['b', 3, 4]]
        task_func(input_data)