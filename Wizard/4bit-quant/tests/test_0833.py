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

    # Test case 4: Invalid input (directory exists but file does not exist)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    assert task_func(filename, data) == False

    # Test case 5: Invalid input (directory exists but file does not exist)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    with open("test/test.pkl", 'wb') as f:
        pickle.dump({"key": "value2"}, f)
    assert task_func(filename, data) == False

    # Test case 6: Invalid input (directory exists but file does not exist)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    with open("test/test.pkl", 'wb') as f:
        pickle.dump({"key": "value2"}, f)
    os.remove("test/test.pkl")
    assert task_func(filename, data) == False

    # Test case 7: Invalid input (directory exists but file does not exist)
    filename = "test/test.pkl"
    data = {"key": "value"}
    os.makedirs("test", exist_ok=True)
    with open("test/test.pkl", 'wb') as f:
        pickle.dump({"key": "value2"}, f)
    os.remove("test/test.pkl")
    os.rmdir("test")
    assert task_func(filename, data) == False