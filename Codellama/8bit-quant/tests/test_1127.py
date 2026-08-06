import pytest
from src_1127 import task_func

def test_task_func():
    input_str = "Hello World!"
    expected_output = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(input_str) == expected_output

def test_task_func_with_special_chars():
    input_str = "Hello World!@#$%^&*()_+-=[]{}|;':\"<>,./?"
    expected_output = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(input_str) == expected_output

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = ""
    assert task_func(input_str) == expected_output

def test_task_func_with_none():
    input_str = None
    expected_output = None
    assert task_func(input_str) == expected_output