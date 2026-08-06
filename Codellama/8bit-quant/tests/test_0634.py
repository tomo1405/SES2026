import pytest
from src_0634 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_output = {'sample': 1, 'testing': 1, 'text': 1, 'function': 1}
    assert task_func(text) == expected_output

def test_task_func_with_duplicate_words():
    text = "This is a sample text for testing the task function. This is a sample text for testing the task function."
    expected_output = {'sample': 2, 'testing': 2, 'text': 2, 'function': 2}
    assert task_func(text) == expected_output

def test_task_func_with_stop_words():
    text = "This is a sample text for testing the task function. The stop words are 'the' and 'a'."
    expected_output = {'sample': 1, 'testing': 1, 'text': 1, 'function': 1}
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = {}
    assert task_func(text) == expected_output

def test_task_func_with_none():
    text = None
    expected_output = {}
    assert task_func(text) == expected_output