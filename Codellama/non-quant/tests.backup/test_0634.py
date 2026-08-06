import pytest
from src_0634 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'for': 1, 'testing': 1, 'the': 1, 'task': 1, 'function': 1}
    assert task_func(text) == expected_output

def test_task_func_with_duplicate_words():
    text = "This is a sample text for testing the task function. This is a sample text for testing the task function."
    expected_output = {'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'text': 2, 'for': 2, 'testing': 2, 'the': 2, 'task': 2, 'function': 2}
    assert task_func(text) == expected_output

def test_task_func_with_stop_words():
    text = "This is a sample text for testing the task function. The task function is a sample text."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'for': 1, 'testing': 1, 'task': 1, 'function': 1}
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = {}
    assert task_func(text) == expected_output

def test_task_func_with_none():
    text = None
    expected_output = {}
    assert task_func(text) == expected_output