import pytest
from src_0750 import task_func
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    expected_output = [0.0, 0.2, 0.4, 0.6, 0.8]

    actual_output = task_func(myList)

    assert np.allclose(actual_output, expected_output)

def test_task_func_with_zero_input():
    myList = [0]
    expected_output = [0.0]

    actual_output = task_func(myList)

    assert np.allclose(actual_output, expected_output)

def test_task_func_with_negative_input():
    myList = [-1, -2, -3]
    expected_output = [0.0, 0.0, 0.0]

    actual_output = task_func(myList)

    assert np.allclose(actual_output, expected_output)