import pytest
from src_0645 import task_func

def test_task_func():
    # Test with valid input
    filename = 'test_file.txt'
    data = 'Hello, World!'
    password = 'password123'
    expected_output = 'U2FsdGVkX18lJQoLbQkJVLQ=='
    output = task_func(filename, data, password)
    assert output == expected_output

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(filename, data, '')

    with pytest.raises(ValueError):
        task_func(filename, '', password)

    with pytest.raises(ValueError):
        task_func('', data, password)