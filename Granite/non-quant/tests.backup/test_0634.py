import pytest
from src_0634 import task_func

def test_task_func():
    text = "This is a sample text. This is another sample text."
    expected_output = {'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'text.': 2, 'another': 1}
    assert task_func(text) == expected_output

def test_task_func_empty_text():
    text = ""
    expected_output = {}
    assert task_func(text) == expected_output

def test_task_func_single_word():
    text = "word"
    expected_output = {'word': 1}
    assert task_func(text) == expected_output

def test_task_func_stopwords():
    text = "This is a sample text. This is another sample text."
    expected_output = {'sample': 2, 'text.': 2}
    assert task_func(text) == expected_output