import pytest
from src_0831 import task_func

def test_task_func_valid_input():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    expected_data = {'key1': 'value1', 'key2': 'value2'}

    result, written_data = task_func(filename, data)

    assert result is True
    assert written_data == expected_data

def test_task_func_invalid_input():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    expected_data = None

    result, written_data = task_func(filename, data)

    assert result is False
    assert written_data == expected_data

def test_task_func_file_exists():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    expected_data = {'key1': 'value1', 'key2': 'value2'}

    result, written_data = task_func(filename, data)

    assert result is True
    assert written_data == expected_data

def test_task_func_file_does_not_exist():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    expected_data = None

    result, written_data = task_func(filename, data)

    assert result is False
    assert written_data == expected_data