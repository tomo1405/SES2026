import os

import pytest
from src_0645 import task_func


def test_task_func():
    # Test that the function raises an error if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('test.txt', 'data', 'password')

    # Test that the function creates the file if it does not exist
    task_func('test.txt', 'data', 'password')
    assert os.path.exists('test.txt')

    # Test that the function encrypts the data using the simple XOR operation
    encrypted = task_func('test.txt', 'data', 'password')
    assert encrypted != 'data'

    # Test that the function writes the encrypted data to the file
    with open('test.txt', 'r') as f:
        assert f.read() == encrypted