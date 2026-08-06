import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_1089 import task_func
import pytest

def test_task_func_with_no_input():
    """
    Test the function with no input data
    """
    expected_output = pd.DataFrame(np.random.rand(100, 5))
    output = task_func()
    assert output.equals(expected_output)

def test_task_func_with_input():
    """
    Test the function with input data
    """
    input_data = np.random.rand(100, 5)
    expected_output = pd.DataFrame(StandardScaler().fit_transform(input_data))
    output = task_func(input_data)
    assert output.equals(expected_output)

def test_task_func_with_negative_values():
    """
    Test the function with negative values in the input data
    """
    input_data = np.random.rand(100, 5)
    input_data[input_data < 0.5] = -1
    expected_output = pd.DataFrame(StandardScaler().fit_transform(input_data))
    output = task_func(input_data)
    assert output.equals(expected_output)