import pytest
from src_0698 import task_func

def test_task_func():
    df = {'feature': [1, 2, 3, 4, 5], 'value': [2, 4, 6, 8, 10]}
    expected_output = {'coefficients': [2.0], 'intercept': [2.0]}
    actual_output = task_func(df)
    assert actual_output == expected_output

def test_task_func_with_different_input():
    df = {'feature': [1, 2, 3, 4, 5], 'value': [1, 4, 9, 16, 25]}
    expected_output = {'coefficients': [4.0], 'intercept': [1.0]}
    actual_output = task_func(df)
    assert actual_output == expected_output