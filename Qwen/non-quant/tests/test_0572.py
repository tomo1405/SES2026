import pytest
from src_0572 import task_func
import pandas as pd
import os

def test_task_func_with_valid_input(tmpdir):
    def example_func(a, b=1, c=2) -> int:
        return a + b + c

    file_path = os.path.join(tmpdir, "test.csv")
    task_func([example_func], file_path)

    expected_data = {
        'Function Name': ['example_func'],
        'Number of Arguments': [3],
        'Defaults': [(1, 2)],
        'Annotations': [{'return': int}],
        'Is Lambda': [False]
    }
    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame(expected_data))

def test_task_func_with_empty_function_list():
    with pytest.raises(ValueError, match="f_list should not be empty."):
        task_func([], "test.csv")

def test_task_func_with_non_callable_element_in_list():
    with pytest.raises(ValueError, match="All elements in f_list must be callable functions."):
        task_func([1, 2, 3], "test.csv")

def test_task_func_with_non_string_file_path():
    def example_func():
        pass

    with pytest.raises(ValueError, match="file_path must be a string."):
        task_func([example_func], 123)

def test_task_func_with_lambda_function(tmpdir):
    lambda_func = lambda x: x * 2
    file_path = os.path.join(tmpdir, "test.csv")
    task_func([lambda_func], file_path)

    expected_data = {
        'Function Name': ['<lambda>'],
        'Number of Arguments': [1],
        'Defaults': [None],
        'Annotations': [{}],
        'Is Lambda': [True]
    }
    df = pd.read_csv(file_path)
    assert df.equals(pd.DataFrame(expected_data))

def test_task_func_with_io_error(tmpdir):
    def example_func():
        pass

    file_path = os.path.join(tmpdir, "test.csv")
    os.chmod(tmpdir, 0o000)  # Make directory read-only to cause an IOError

    with pytest.raises(IOError, match="Error writing to file: "):
        task_func([example_func], file_path)

    os.chmod(tmpdir, 0o777)  # Restore directory permissions