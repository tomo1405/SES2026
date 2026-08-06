import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is a sample text [with brackets]."
    expected_result = {"This": 0.5, "is": 0.5, "a": 0.5, "sample": 0.5, "text": 0.5, "with": 0.5, "brackets": 0.5}
    assert task_func(example_str) == expected_result

def test_task_func_empty_string():
    example_str = ""
    expected_result = {}
    assert task_func(example_str) == expected_result

def test_task_func_no_brackets():
    example_str = "This is a sample text."
    expected_result = {"This": 0.5, "is": 0.5, "a": 0.5, "sample": 0.5, "text": 0.5}
    assert task_func(example_str) == expected_result

def test_task_func_multiple_brackets():
    example_str = "This is a sample text [with brackets] [and more brackets]."
    expected_result = {"This": 0.5, "is": 0.5, "a": 0.5, "sample": 0.5, "text": 0.5, "with": 0.5, "brackets": 0.5, "and": 0.5, "more": 0.5, "brackets": 0.5}
    assert task_func(example_str) == expected_result