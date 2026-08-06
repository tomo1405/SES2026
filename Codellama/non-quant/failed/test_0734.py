import pytest
from src_0734 import task_func

def test_task_func():
    content = "This is a test sentence."
    assert task_func(content) == 4

def test_task_func_with_stopwords():
    content = "This is a test sentence with stopwords."
    assert task_func(content) == 4

def test_task_func_with_punctuation():
    content = "This is a test sentence with punctuation."
    assert task_func(content) == 4

def test_task_func_with_empty_string():
    content = ""
    assert task_func(content) == 0

def test_task_func_with_single_word():
    content = "test"
    assert task_func(content) == 1

def test_task_func_with_multiple_words():
    content = "test sentence"
    assert task_func(content) == 2