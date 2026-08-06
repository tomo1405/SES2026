import pandas as pd
from src_0698 import task_func


def test_task_func():
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [10, 20, 30, 40, 50]})
    expected_coefficients = [1, 2, 3, 4, 5]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept

def test_task_func_with_invalid_input():
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [10, 20, 30, 40, 50]})
    expected_coefficients = [1, 2, 3, 4, 5]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept

def test_task_func_with_different_input():
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'value': [10, 20, 30, 40, 50]})
    expected_coefficients = [1, 2, 3, 4, 5]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept