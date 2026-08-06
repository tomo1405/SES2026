import pytest
from src_0377 import task_func

def test_task_func_with_no_words():
    text = ""
    assert task_func(text) == {}

def test_task_func_with_only_stopwords():
    text = "and the of in"
    assert task_func(text) == {}

def test_task_func_with_single_word():
    text = "Hello"
    assert task_func(text) == {'hello': 1}

def test_task_func_with_multiple_words():
    text = "Hello world! Hello everyone."
    assert task_func(text) == {'hello': 2, 'world': 1, 'everyone': 1}

def test_task_func_with_punctuation():
    text = "Hello, world! This is a test."
    assert task_func(text) == {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}

def test_task_func_with_case_insensitivity():
    text = "HELLO hello HeLLo"
    assert task_func(text) == {'hello': 3}

def test_task_func_with_numbers():
    text = "Hello 123 world"
    assert task_func(text) == {'hello': 1, 'world': 1}