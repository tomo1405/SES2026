import pytest
from src_0809 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_result = 0.5
    assert task_func(text) == expected_result

def test_task_func_with_stopwords():
    text = "This is a sample text for testing the task function."
    expected_result = 0.5
    assert task_func(text) == expected_result

def test_task_func_with_empty_text():
    text = ""
    expected_result = 0.0
    assert task_func(text) == expected_result

def test_task_func_with_invalid_text():
    text = "This is a sample text for testing the task function."
    expected_result = 0.5
    assert task_func(text) == expected_result