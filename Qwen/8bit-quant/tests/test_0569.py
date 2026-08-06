import pandas as pd
import pytest
from src_0569 import task_func


def test_task_func_with_valid_functions():
    def func1(x):
        return x + 1

    def func2(x, y):
        return x + y

    expected_df = pd.DataFrame({
        'Function Name': ['func1', 'func2'],
        'Number of Arguments': [1, 2]
    }).set_index('Function Name')

    result_df = task_func([func1, func2])
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_lambda_function():
    with pytest.raises(ValueError) as excinfo:
        task_func([lambda x: x + 1])

    assert str(excinfo.value) == "The function should not be a lambda function."

def test_task_func_with_no_functions():
    expected_df = pd.DataFrame(columns=['Function Name', 'Number of Arguments']).set_index('Function Name')
    result_df = task_func([])
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_single_function():
    def func3(a, b, c):
        return a + b + c

    expected_df = pd.DataFrame({
        'Function Name': ['func3'],
        'Number of Arguments': [3]
    }).set_index('Function Name')

    result_df = task_func([func3])
    pd.testing.assert_frame_equal(result_df, expected_df)