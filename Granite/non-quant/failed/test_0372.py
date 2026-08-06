import pytest
from src_0372 import task_func
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def test_task_func():
    # Test case 1: Test with a list of integers
    l = [1, 2, 3, 4, 5]
    expected_output = pd.DataFrame([[0.0], [0.2], [0.4], [0.6], [0.8]], columns=['Scaled Values'])
    actual_output = task_func(l)
    assert actual_output.equals(expected_output)

    # Test case 2: Test with a list of floating-point numbers
    l = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = pd.DataFrame([[0.0], [0.2], [0.4], [0.6], [0.8]], columns=['Scaled Values'])
    actual_output = task_func(l)
    assert actual_output.equals(expected_output)

    # Test case 3: Test with an empty list
    l = []
    expected_output = pd.DataFrame(columns=['Scaled Values'])
    actual_output = task_func(l)
    assert actual_output.equals(expected_output)

    # Test case 4: Test with a list of negative numbers
    l = [-1, -2, -3, -4, -5]
    expected_output = pd.DataFrame([[-1.0], [-0.8], [-0.6], [-0.4], [-0.2]], columns=['Scaled Values'])
    actual_output = task_func(l)
    assert actual_output.equals(expected_output)