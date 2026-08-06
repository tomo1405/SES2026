import pytest
from src_0271 import task_func

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_single_word():
    assert task_func("hello") == {"hello": 1}

def test_task_func_multiple_words():
    assert task_func("hello world hello") == {"hello": 2, "world": 1}

def test_task_func_case_insensitivity():
    assert task_func("Hello hello") == {"Hello": 1, "hello": 1}

def test_task_func_punctuation():
    assert task_func("Hello, world!") == {"Hello": 1, "world": 1}

def test_task_func_numbers():
    assert task_func("123 456 123") == {"123": 2, "456": 1}

def test_task_func_mixed_case_and_numbers():
    assert task_func("Hello 123 hello 123") == {"Hello": 1, "hello": 1, "123": 2}