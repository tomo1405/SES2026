import pytest
from src_0372 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    l = [1, 2, 3, 4, 5]
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.5, 1.0, 1.5, 2.0]}, dtype=float)
    assert task_func(l).equals(expected_output)

def test_task_func_with_different_input():
    l = [1, 2, 3, 4, 5, 6]
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]}, dtype=float)
    assert task_func(l).equals(expected_output)

def test_task_func_with_negative_input():
    l = [-1, -2, -3, -4, -5]
    expected_output = pd.DataFrame({'Scaled Values': [-1.0, -0.5, 0.0, 0.5, 1.0]}, dtype=float)
    assert task_func(l).equals(expected_output)

def test_task_func_with_zero_input():
    l = [0, 0, 0, 0, 0]
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.0, 0.0, 0.0, 0.0]}, dtype=float)
    assert task_func(l).equals(expected_output)