import os

import pytest
from src_0874 import task_func


def test_task_func_valid_input():
    data = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    file_path = 'test_data.csv'
    headers = ['col1', 'col2', 'col3']
    expected_output = os.path.abspath(file_path)

    output = task_func(data, file_path, headers)

    assert output == expected_output

def test_task_func_invalid_file_path():
    data = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    file_path = None
    headers = ['col1', 'col2', 'col3']

    with pytest.raises(ValueError):
        task_func(data, file_path, headers)

def test_task_func_invalid_headers():
    data = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    file_path = 'test_data.csv'
    headers = ['col1', 'col2', 'col3', 'col4']

    with pytest.raises(ValueError):
        task_func(data, file_path, headers)

def test_task_func_invalid_data():
    data = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    file_path = 'test_data.csv'
    headers = ['col1', 'col2', 'col3']

    with pytest.raises(ValueError):
        task_func(data, file_path, headers)