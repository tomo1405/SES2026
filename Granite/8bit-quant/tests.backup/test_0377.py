import pytest
from src_0377 import task_func

def test_task_func():
    text = "This is a sample text for testing."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'for': 1, 'testing': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_empty_text():
    text = ""
    expected_output = {}
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_only_stopwords():
    text = "This is a sample text for testing stopwords."
    expected_output = {}
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function output does not match expected output."