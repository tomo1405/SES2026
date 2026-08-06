import pytest
from src_0190 import task_func

def test_task_func_valid_url():
    data_url = "https://jsonplaceholder.typicode.com/users"
    expected_output = ["typicode", "msn", "jsonplaceholder"]
    actual_output = task_func(data_url)
    assert actual_output == expected_output

def test_task_func_invalid_url():
    data_url = "invalid_url"
    expected_output = "Invalid url input"
    actual_output = task_func(data_url)
    assert actual_output == expected_output

def test_task_func_empty_url():
    data_url = ""
    expected_output = "Invalid url input"
    actual_output = task_func(data_url)
    assert actual_output == expected_output