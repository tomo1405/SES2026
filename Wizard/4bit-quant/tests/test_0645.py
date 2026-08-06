python
import hashlib
import base64
import os
import pytest

from src_0645 import task_func

def test_task_func():
    # Test case 1: Valid input
    filename = 'test.txt'
    data = 'Hello, world!'
    password = 'password'
    encrypted = task_func(filename, data, password)
    assert encrypted == 'SGVsbG8sIHdvcmxkIQ=='

    # Test case 2: Invalid input (empty data)
    with pytest.raises(ValueError):
        task_func(filename, '', password)

    # Test case 3: Invalid input (empty password)
    with pytest.raises(ValueError):
        task_func(filename, data, '')

    # Test case 4: Invalid input (non-existent directory)
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent/test.txt', data, password)

    # Test case 5: Invalid input (non-existent file)
    with pytest.raises(FileNotFoundError):
        task_func('test.txt', data, password)

    # Test case 6: Invalid input (invalid directory)
    with pytest.raises(NotADirectoryError):
        task_func('test.txt', data, password, directory='/etc')

    # Test case 7: Invalid input (invalid file)
    with pytest.raises(IsADirectoryError):
        task_func('test.txt', data, password, filename='test')

    # Test case 8: Invalid input (invalid data)
    with pytest.raises(TypeError):
        task_func(filename, 123, password)

    # Test case 9: Invalid input (invalid password)
    with pytest.raises(TypeError):
        task_func(filename, data, 123)

    # Test case 10: Invalid input (invalid directory)
    with pytest.raises(TypeError):
        task_func(filename, data, password, directory=123)

    # Test case 11: Invalid input (invalid file)
    with pytest.raises(TypeError):
        task_func(filename, data, password, filename=123)