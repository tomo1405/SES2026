import pytest
from src_0938 import task_func
from collections import Counter

def test_task_func():
    input_str = "Hello, World! 123"
    expected_output = Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '1': 1, '2': 1, '3': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output

def test_task_func_empty_string():
    input_str = ""
    expected_output = Counter({})
    actual_output = task_func(input_str)
    assert actual_output == expected_output

def test_task_func_only_numbers():
    input_str = "12345"
    expected_output = Counter({'1': 1, '2': 1, '3': 1, '4': 1, '5': 1})
    actual_output = task_func(input_str)
    assert actual_output == expected_output