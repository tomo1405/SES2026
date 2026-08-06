import pytest
from src_0572 import task_func
import pandas as pd

def test_task_func_with_valid_input():
    def sample_function(a, b, c=1):
        return a + b + c

    file_path = "test_output.csv"
    task_func([sample_function], file_path)

    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame({
        'Function Name': ['sample_function'],
        'Number of Arguments': [3],
        'Defaults': [[1]],
        'Annotations': [{}],
        'Is Lambda': [False]
    }))

def test_task_func_with_empty_f_list():
    with pytest.raises(ValueError, match="f_list should not be empty."):
        task_func([], "test_output.csv")

def test_task_func_with_non_callable_element_in_f_list():
    with pytest.raises(ValueError, match="All elements in f_list must be callable functions."):
        task_func([123], "test_output.csv")

def test_task_func_with_non_string_file_path():
    def sample_function(a, b, c=1):
        return a + b + c

    with pytest.raises(ValueError, match="file_path must be a string."):
        task_func([sample_function], 123)

def test_task_func_with_lambda_function():
    lambda_func = lambda x, y: x + y
    file_path = "test_output.csv"
    task_func([lambda_func], file_path)

    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame({
        'Function Name': ['<lambda>'],
        'Number of Arguments': [2],
        'Defaults': [None],
        'Annotations': [{}],
        'Is Lambda': [True]
    }))

def test_task_func_with_io_error():
    def sample_function(a, b, c=1):
        return a + b + c

    file_path = "/nonexistent/directory/test_output.csv"
    with pytest.raises(IOError, match="Error writing to file: "):
        task_func([sample_function], file_path)