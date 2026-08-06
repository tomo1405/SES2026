import pytest
from src_0852 import task_func

def test_task_func_single_line():
    input_string = "This is a test string."
    width = 10
    expected_output = "This was a\ntest string."
    assert task_func(input_string, width) == expected_output

def test_task_func_multiple_lines():
    input_string = "This is the first line.\nThis is the second line."
    width = 10
    expected_output = "This was the\nfirst line.\nThis was the\nsecond line."
    assert task_func(input_string, width) == expected_output

def test_task_func_no_wrap():
    input_string = "Short line"
    width = 20
    expected_output = "Short line"
    assert task_func(input_string, width) == expected_output

def test_task_func_long_word():
    input_string = "A verylongwordthatwillnotbreak"
    width = 10
    expected_output = "A verylongwordthatwillnotbreak"
    assert task_func(input_string, width) == expected_output

def test_task_func_empty_string():
    input_string = ""
    width = 10
    expected_output = ""
    assert task_func(input_string, width) == expected_output

def test_task_func_no_is():
    input_string = "There is no 'is' here."
    width = 10
    expected_output = "There was no\n'was' here."
    assert task_func(input_string, width) == expected_output

def test_task_func_is_at_end():
    input_string = "This is at the end"
    width = 10
    expected_output = "This was at\nthe end"
    assert task_func(input_string, width) == expected_output

def test_task_func_is_at_start():
    input_string = "Is this at the start?"
    width = 10
    expected_output = "Was this at\nthe start?"
    assert task_func(input_string, width) == expected_output