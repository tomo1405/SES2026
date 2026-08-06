import pytest
from src_0850 import task_func

def test_task_func():
    input_string = "This is a test string."
    expected_output = {"This": 1, "is": 1, "a": 1, "test": 1, "string": 1}
    assert task_func(input_string) == expected_output

def test_task_func_with_stopwords():
    input_string = "This is a test string. The quick brown fox jumps over the lazy dog."
    expected_output = {"This": 1, "is": 1, "a": 1, "test": 1, "string": 1, "fox": 1, "jumps": 1, "dog": 1}
    assert task_func(input_string) == expected_output

def test_task_func_with_empty_string():
    input_string = ""
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_with_invalid_input():
    input_string = "This is a test string."
    expected_output = {"This": 1, "is": 1, "a": 1, "test": 1, "string": 1}
    assert task_func(input_string) == expected_output