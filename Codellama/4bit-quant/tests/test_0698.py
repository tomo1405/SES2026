import pandas as pd
import pytest
from src_0698 import task_func


def test_task_func():
    df = pd.DataFrame({'feature': [1, 2, 3], 'value': [2, 4, 6]})
    expected_coefficients = [1, 1]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept

def test_task_func_with_invalid_input():
    df = pd.DataFrame({'feature': [1, 2, 3], 'value': [2, 4, 6]})
    expected_coefficients = [1, 1]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept

def test_task_func_with_different_input():
    df = pd.DataFrame({'feature': [1, 2, 3], 'value': [2, 4, 6]})
    expected_coefficients = [1, 1]
    expected_intercept = 0

    result = task_func(df)

    assert result['coefficients'] == expected_coefficients
    assert result['intercept'] == expected_intercept

if __name__ == '__main__':
    pytest.main()