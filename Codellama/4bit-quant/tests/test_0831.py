import pytest
from src_0831 import task_func

def test_task_func():
    # Test with valid input
    filename = 'test_data.json'
    data = {'name': 'John Doe', 'age': 30}
    result, written_data = task_func(filename, data)
    assert result is True
    assert written_data == data

    # Test with invalid input
    filename = 'test_data.json'
    data = {'name': 'John Doe', 'age': 'invalid'}
    result, written_data = task_func(filename, data)
    assert result is False
    assert written_data is None

    # Test with missing file
    filename = 'missing_file.json'
    data = {'name': 'John Doe', 'age': 30}
    result, written_data = task_func(filename, data)
    assert result is False
    assert written_data is None