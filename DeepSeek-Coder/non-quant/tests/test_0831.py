import pytest
from src_0831 import task_func
import os
import json

@pytest.fixture
def setup_and_teardown():
    test_filename = "test_file.json"
    test_data = {"key": "value"}
    yield test_filename, test_data
    os.remove(test_filename)

def test_task_func(setup_and_teardown):
    filename, data = setup_and_teardown
    result, _ = task_func(filename, data)
    assert result is True

def test_task_func_invalid_data(setup_and_teardown):
    filename, data = setup_and_teardown
    data["invalid_key"] = "invalid_value"
    result, _ = task_func(filename, data)
    assert result is False

def test_task_func_file_not_created(setup_and_teardown):
    filename, data = setup_and_teardown
    os.remove(filename)
    result, _ = task_func(filename, data)
    assert result is False