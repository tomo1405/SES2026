import pandas as pd
import pytest
from src_0510 import task_func


def test_task_func_valid_input():
    file_path1 = 'file1.csv'
    file_path2 = 'file2.csv'
    delimiter = ','
    quotechar = '"'
    expected_output = pd.DataFrame({'Line Number': [1, 2, 3], 'Status': ['added', 'removed', 'changed'], 'Content': ['a', 'b', 'c']})
    actual_output = task_func(file_path1, file_path2, delimiter, quotechar)
    assert actual_output.equals(expected_output)

def test_task_func_invalid_input():
    file_path1 = 'file1.csv'
    file_path2 = 'file2.csv'
    delimiter = ','
    quotechar = '"'
    with pytest.raises(ValueError):
        task_func(file_path1, file_path2, delimiter, quotechar)

def test_task_func_empty_file():
    file_path1 = 'file1.csv'
    file_path2 = 'file2.csv'
    delimiter = ','
    quotechar = '"'
    with pytest.raises(ValueError):
        task_func(file_path1, file_path2, delimiter, quotechar)

def test_task_func_file_not_found():
    file_path1 = 'file1.csv'
    file_path2 = 'file2.csv'
    delimiter = ','
    quotechar = '"'
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2, delimiter, quotechar)