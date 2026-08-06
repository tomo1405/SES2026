import pytest
from src_0735 import task_func
from collections import Counter

def test_task_func_with_empty_string():
    assert task_func("") == {}

def test_task_func_with_single_word():
    assert task_func("hello") == {}

def test_task_func_with_simple_sentence():
    result = task_func("hello world")
    assert result == {'NN': 1}

def test_task_func_with_multiple_sentences():
    result = task_func("hello world! this is a test.")
    assert result == {'NN': 2, 'DT': 1, 'VBZ': 1, 'JJ': 1}

def test_task_func_with_punctuation():
    result = task_func("hello, world!")
    assert result == {'NN': 1}

def test_task_func_with_numbers():
    result = task_func("hello 123 world")
    assert result == {'NN': 2}

def test_task_func_with_repeated_words():
    result = task_func("hello hello world")
    assert result == {'NN': 2}