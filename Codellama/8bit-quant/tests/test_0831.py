import json
import os

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
    result, written_data = task_func(filename, data)
    assert result is False
    assert written_data is None

def test_task_func_file_exists():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    result, written_data = task_func(filename, data)
    assert os.path.exists(filename) is True

def test_task_func_file_not_exists():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    result, written_data = task_func(filename, data)
    assert os.path.exists(filename) is False

def test_task_func_file_content():
    filename = 'test_file.json'
    data = {'key1': 'value1', 'key2': 'value2'}
    result, written_data = task_func(filename, data)
    with open(filename, 'r') as f:
        written_data = json.load(f)
        assert written_data == data