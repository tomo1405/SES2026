import pytest
from src_1100 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_result = [('sample', 1), ('text', 1), ('testing', 1), ('task', 1), ('function', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_stopwords():
    text = "This is a sample text for testing the task function."
    expected_result = [('sample', 1), ('text', 1), ('testing', 1), ('task', 1), ('function', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_no_stopwords():
    text = "This is a sample text for testing the task function."
    expected_result = [('sample', 1), ('text', 1), ('testing', 1), ('task', 1), ('function', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_empty_string():
    text = ""
    expected_result = []
    assert task_func(text) == expected_result

def test_task_func_with_none():
    text = None
    expected_result = []
    assert task_func(text) == expected_result