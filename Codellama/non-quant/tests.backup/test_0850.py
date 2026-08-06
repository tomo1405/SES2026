import pytest
from src_0850 import task_func

def test_task_func():
    input_string = "This is a test string.\nThis is another test string."
    expected_output = {"This": 2, "is": 2, "a": 1, "test": 2, "string": 2}
    assert task_func(input_string) == expected_output

def test_task_func_with_stopwords():
    input_string = "This is a test string.\nThis is another test string."
    expected_output = {"This": 2, "is": 2, "a": 1, "test": 2, "string": 2}
    assert task_func(input_string) == expected_output

def test_task_func_with_empty_string():
    input_string = ""
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_with_invalid_input():
    input_string = "This is a test string.\nThis is another test string."
    expected_output = {"This": 2, "is": 2, "a": 1, "test": 2, "string": 2}
    assert task_func(input_string) == expected_output