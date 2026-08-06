import pytest
from src_0941 import task_func
from collections import Counter

def test_task_func_with_empty_string():
    assert task_func("") == Counter()

def test_task_func_with_single_word():
    assert task_func("hello") == Counter({'hello': 1})

def test_task_func_with_multiple_words():
    assert task_func("hello world hello") == Counter({'hello': 2, 'world': 1})

def test_task_func_with_punctuation():
    assert task_func("hello, world!") == Counter({'hello': 1, 'world': 1})

def test_task_func_with_numbers():
    assert task_func("hello 123 world 123") == Counter({'hello': 1, '123': 2, 'world': 1})

def test_task_func_with_mixed_case():
    assert task_func("Hello World hello") == Counter({'Hello': 1, 'World': 1, 'hello': 1})

def test_task_func_with_special_characters():
    assert task_func("hello@world#123") == Counter({'hello': 1, 'world': 1, '123': 1})