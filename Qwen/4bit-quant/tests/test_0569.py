import pytest
from src_0569 import task_func
import inspect
import pandas as pd

def test_task_func_with_non_lambda_functions():
    def example_func1(a, b):
        pass

    def example_func2(x, y, z):
        pass

    result_df = task_func([example_func1, example_func2])
    expected_data = {
        'Function Name': ['example_func1', 'example_func2'],
        'Number of Arguments': [2, 3]
    }
    expected_df = pd.DataFrame(expected_data).set_index('Function Name')
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_lambda_function():
    with pytest.raises(ValueError):
        task_func([lambda x: x + 1])

def test_task_func_with_no_functions():
    result_df = task_func([])
    expected_data = {
        'Function Name': [],
        'Number of Arguments': []
    }
    expected_df = pd.DataFrame(expected_data).set_index('Function Name')
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_single_function():
    def single_func(arg1):
        pass

    result_df = task_func([single_func])
    expected_data = {
        'Function Name': ['single_func'],
        'Number of Arguments': [1]
    }
    expected_df = pd.DataFrame(expected_data).set_index('Function Name')
    pd.testing.assert_frame_equal(result_df, expected_df)