import pytest
from src_0941 import task_func

def test_task_func():
    input_str = "Hello, World!"
    expected_output = {"Hello": 1, "World": 1}
    assert task_func(input_str) == expected_output

def test_task_func_with_empty_input():
    input_str = ""
    expected_output = {}
    assert task_func(input_str) == expected_output

def test_task_func_with_invalid_input():
    input_str = "Hello, World!"
    expected_output = {"Hello": 1, "World": 1}
    assert task_func(input_str) == expected_output

def test_task_func_with_multiple_words():
    input_str = "Hello, World! How are you?"
    expected_output = {"Hello": 1, "World": 1, "How": 1, "are": 1, "you": 1}
    assert task_func(input_str) == expected_output