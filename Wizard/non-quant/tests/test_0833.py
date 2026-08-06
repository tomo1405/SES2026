python
import os
import pickle
import pytest

from src_0833 import task_func

def test_task_func():
    # Test case 1: Valid input
    filename = "test.pkl"
    data = {"key": "value"}
    assert task_func(filename, data) == True
    assert os.path.exists(filename) == True
    with open(filename, 'rb') as f:
        assert pickle.load(f) == data

    # Test case 2: Invalid input (empty filename)
    filename = ""
    data = {"key": "value"}
    assert task_func(filename, data) == False

    # Test case 3: Invalid input (directory does not exist)
    filename = "test/test.pkl"
    data = {"key": "value"}
    assert task_func(filename, data) == False

    # Test case 4: Invalid input (directory exists but file does not)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    assert task_func(filename, data) == False

    # Test case 5: Invalid input (directory exists and file exists)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    assert task_func(filename, data) == False