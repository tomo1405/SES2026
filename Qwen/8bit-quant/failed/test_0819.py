import pytest
from src_0819 import task_func

def test_task_func_with_no_punctuation():
    text = "Hello world"
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

def test_task_func_with_punctuation():
    text = "Hello, world!"
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

def test_task_func_with_multiple_spaces():
    text = "  Hello   world  "
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_only_punctuation():
    text = "!@#$%^&*()"
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_mixed_content():
    text = "Hello, World! This is a Test."
    expected_output = ["hello", "world", "this", "is", "a", "test"]
    assert task_func(text) == expected_output