import pytest
from src_0941 import task_func
from nltk import word_tokenize
from collections import Counter

def test_task_func_empty_string():
    assert task_func("") == Counter()

def test_task_func_no_words():
    assert task_func("!!!@@@###$$$") == Counter()

def test_task_func_single_word():
    assert task_func("hello") == Counter({'hello': 1})

def test_task_func_multiple_words():
    assert task_func("hello world hello") == Counter({'hello': 2, 'world': 1})

def test_task_func_case_insensitivity():
    assert task_func("Hello hello HELLO") == Counter({'hello': 3})

def test_task_func_with_numbers():
    assert task_func("hello 123 world 123") == Counter({'hello': 1, '123': 2, 'world': 1})

def test_task_func_punctuation():
    assert task_func("hello, world!") == Counter({'hello': 1, 'world': 1})

def test_task_func_mixed_content():
    assert task_func("Hello, world! 123 456 Hello") == Counter({'hello': 2, 'world': 1, '123': 1, '456': 1})