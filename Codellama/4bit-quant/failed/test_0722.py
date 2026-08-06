import pytest
from src_0722 import task_func

def test_task_func_with_valid_file():
    file_path = 'test_data.csv'
    expected_result = ('word', 10)
    result = task_func(file_path)
    assert result == expected_result

def test_task_func_with_invalid_file():
    file_path = 'invalid_file.csv'
    expected_result = None
    result = task_func(file_path)
    assert result == expected_result

def test_task_func_with_empty_file():
    file_path = 'empty_file.csv'
    expected_result = None
    result = task_func(file_path)
    assert result == expected_result