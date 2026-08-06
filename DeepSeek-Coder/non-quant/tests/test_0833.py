import pytest
from src_0833 import task_func
import os
import pickle

@pytest.fixture
def setup_and_teardown():
    # Setup code here
    yield
    # Teardown code here

def test_task_func_success(setup_and_teardown):
    filename = "test_file.pkl"
    data = {"key": "value"}
    result = task_func(filename, data)
    assert result is True
    with open(filename, 'rb') as f:
        loaded_data = pickle.load(f)
    assert loaded_data == data
    os.remove(filename)

def test_task_func_failure(setup_and_teardown):
    filename = "test_file.pkl"
    data = "invalid_data"
    result = task_func(filename, data)
    assert result is False
    assert not os.path.exists(filename)