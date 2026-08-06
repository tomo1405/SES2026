import pytest
from src_0271 import task_func

def test_task_func_with_empty_string():
    assert task_func("") == {}

def test_task_func_with_single_word():
    assert task_func("hello") == {"hello": 1}

def test_task_func_with_multiple_words():
    assert task_func("hello world hello") == {"hello": 2, "world": 1}

def test_task_func_with_punctuation():
    assert task_func("hello, world!") == {"hello": 1, "world": 1}

def test_task_func_with_case_insensitivity():
    assert task_func("Hello hello") == {"Hello": 1, "hello": 1}

def test_task_func_with_numbers():
    assert task_func("hello 123 world 123") == {"hello": 1, "123": 2, "world": 1}

def test_task_func_with_special_characters():
    assert task_func("@hello! #world$") == {"hello": 1, "world": 1}