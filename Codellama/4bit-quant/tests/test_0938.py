import pytest
from src_0938 import task_func

def test_task_func():
    input_str = "Hello, World!"
    expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(input_str) == expected_output

def test_task_func_empty_input():
    input_str = ""
    expected_output = {}
    assert task_func(input_str) == expected_output

def test_task_func_invalid_input():
    input_str = "Hello, World!"
    expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(input_str) == expected_output

def test_task_func_invalid_input_2():
    input_str = "Hello, World!"
    expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert task_func(input_str) == expected_output