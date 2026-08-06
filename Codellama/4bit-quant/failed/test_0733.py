import pytest
from src_0733 import task_func

def test_task_func():
    content = "This is a test sentence."
    expected_result = {"test": 1, "is": 2, "a": 1, "sentence": 1}
    assert task_func(content) == expected_result

def test_task_func_empty_input():
    content = ""
    expected_result = {}
    assert task_func(content) == expected_result

def test_task_func_invalid_input():
    content = "This is a test sentence."
    expected_result = {}
    assert task_func(content) == expected_result