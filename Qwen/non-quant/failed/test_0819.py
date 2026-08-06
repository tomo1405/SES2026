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

def test_task_func_with_multiple_punctuation():
    text = "Hello!!! world..."
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

def test_task_func_with_mixed_case():
    text = "Hello, WORLD!"
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_only_spaces():
    text = "   "
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_special_characters():
    text = "Hello @world! #Python"
    expected_output = ["hello", "world", "python"]
    assert task_func(text) == expected_output

def test_task_func_with_numbers():
    text = "Hello 123 world 456"
    expected_output = ["hello", "world"]
    assert task_func(text) == expected_output