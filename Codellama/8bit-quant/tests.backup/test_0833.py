import pytest
from src_0833 import task_func

def test_task_func_valid_input():
    filename = "test_file.pkl"
    data = {"key": "value"}
    assert task_func(filename, data) == True

def test_task_func_invalid_input():
    filename = "test_file.pkl"
    data = {"key": "value"}
    with pytest.raises(Exception):
        task_func(filename, data)