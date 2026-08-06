import pytest
from src_0034 import task_func
import numpy as np

def test_task_func_with_positive_numbers():
    input_data = [(1, 2), (3, 4), (5, 6)]
    expected_output = np.array([48])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_zero():
    input_data = [(1, 0), (3, 4), (5, 6)]
    expected_output = np.array([0])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_negative_numbers():
    input_data = [(1, -2), (3, 4), (5, -6)]
    expected_output = np.array([288])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_single_pair():
    input_data = [(1, 2)]
    expected_output = np.array([2])
    assert np.array_equal(task_func(input_data), expected_output)

def test_task_func_with_empty_list():
    input_data = []
    with pytest.raises(IndexError):
        task_func(input_data)