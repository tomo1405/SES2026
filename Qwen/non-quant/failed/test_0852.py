import pytest
from src_0852 import task_func

def test_task_func_basic():
    input_string = "This is a test string that needs to be wrapped."
    width = 10
    expected_output = "This was a\ntest string\nthat needs to\nbe wrapped."
    assert task_func(input_string, width) == expected_output

def test_task_func_no_wrap_needed():
    input_string = "Short string"
    width = 20
    expected_output = "Short string"
    assert task_func(input_string, width) == expected_output

def test_task_func_long_word():
    input_string = "Thisisaverylongwordthatneedstobewrapped."
    width = 10
    expected_output = "Thisisaverylongwordthatneedstobewrapped."
    assert task_func(input_string, width) == expected_output

def test_task_func_multiple_lines():
    input_string = "First line.\nSecond line with more text."
    width = 15
    expected_output = "First line.\nSecond line\nwith more text."
    assert task_func(input_string, width) == expected_output

def test_task_func_empty_string():
    input_string = ""
    width = 10
    expected_output = ""
    assert task_func(input_string, width) == expected_output

def test_task_func_no_is():
    input_string = "There is no 'is' here."
    width = 20
    expected_output = "There was no 'was' here."
    assert task_func(input_string, width) == expected_output

def test_task_func_only_is():
    input_string = "is is is"
    width = 10
    expected_output = "was was was"
    assert task_func(input_string, width) == expected_output