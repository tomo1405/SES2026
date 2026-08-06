import pytest
from src_0377 import task_func

def test_task_func():
    text = "This is a sample text for testing the task function."
    expected_result = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'for': 1, 'testing': 1, 'the': 1, 'task': 1, 'function': 1}
    assert task_func(text) == expected_result

def test_task_func_with_stopwords():
    text = "This is a sample text for testing the task function."
    expected_result = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'for': 1, 'testing': 1, 'the': 1, 'task': 1, 'function': 1}
    assert task_func(text) == expected_result

def test_task_func_with_empty_string():
    text = ""
    expected_result = {}
    assert task_func(text) == expected_result

def test_task_func_with_stopwords_and_empty_string():
    text = ""
    expected_result = {}
    assert task_func(text) == expected_result