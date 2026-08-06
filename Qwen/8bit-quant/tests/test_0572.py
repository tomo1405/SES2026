import pytest
from src_0572 import task_func
import pandas as pd
import os

def test_task_func_with_valid_input():
    def func1(a, b):
        return a + b

    def func2(x=1, y=2):
        return x * y

    file_path = "test_output.csv"
    task_func([func1, func2], file_path)

    expected_data = [
        ['func1', 2, None, {}, False],
        ['func2', 2, (1, 2), {}, False]
    ]
    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame(expected_data, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda']))

    # Clean up the test file
    os.remove(file_path)

def test_task_func_with_empty_function_list():
    with pytest.raises(ValueError, match="f_list should not be empty."):
        task_func([], "test_output.csv")

def test_task_func_with_non_callable_elements():
    with pytest.raises(ValueError, match="All elements in f_list must be callable functions."):
        task_func([1, 2, 3], "test_output.csv")

def test_task_func_with_non_string_file_path():
    def func():
        pass
    with pytest.raises(ValueError, match="file_path must be a string."):
        task_func([func], 123)

def test_task_func_with_lambda_function():
    def func1(a, b):
        return a + b

    lambda_func = lambda x, y: x * y

    file_path = "test_output.csv"
    task_func([func1, lambda_func], file_path)

    expected_data = [
        ['func1', 2, None, {}, False],
        [lambda_func.__name__, 2, None, {}, True]
    ]
    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame(expected_data, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda']))

    # Clean up the test file
    os.remove(file_path)

def test_task_func_with_io_error():
    def func():
        pass

    file_path = "/nonexistent/path/test_output.csv"
    with pytest.raises(IOError, match="Error writing to file: "):
        task_func([func], file_path)