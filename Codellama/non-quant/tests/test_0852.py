import pytest
from src_0852 import task_func

def test_task_func():
    input_string = "This is a test string"
    width = 10
    expected_output = "This was a test string"
    assert task_func(input_string, width) == expected_output

def test_task_func_with_long_word():
    input_string = "This is a very long test string"
    width = 10
    expected_output = "This was a very long test string"
    assert task_func(input_string, width) == expected_output

def test_task_func_with_multiple_lines():
    input_string = "This is a test string\nThis is another test string"
    width = 10
    expected_output = "This was a test string\nThis was another test string"
    assert task_func(input_string, width) == expected_output

def test_task_func_with_long_word_and_multiple_lines():
    input_string = "This is a very long test string\nThis is another very long test string"
    width = 10
    expected_output = "This was a very long test string\nThis was another very long test string"
    assert task_func(input_string, width) == expected_output