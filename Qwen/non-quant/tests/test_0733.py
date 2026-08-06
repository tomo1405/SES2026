import pytest
from src_0733 import task_func
from nltk.stem import PorterStemmer
from collections import Counter

# Ensure the stemmer is initialized
STEMMER = PorterStemmer()

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_single_word():
    assert task_func("hello") == {'hello': 1}

def test_task_func_multiple_words():
    assert task_func("hello world hello") == {'hello': 2, 'world': 1}

def test_task_func_punctuation():
    assert task_func("hello, world!") == {'hello': 1, 'world': 1}

def test_task_func_stemming():
    assert task_func("running runs run") == {'run': 3}

def test_task_func_case_insensitivity():
    assert task_func("Hello hello HELLO") == {'hello': 3}

def test_task_func_special_characters():
    assert task_func("$$$hello!!!") == {'hello': 1}

def test_task_func_large_input():
    input_text = " ".join(["word"] * 1000)
    expected_output = {'word': 1000}
    assert task_func(input_text) == expected_output

def test_task_func_mixed_content():
    input_text = "Hello, world! This is a test. Testing, one, two, three."
    expected_output = {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 2, 'testing': 1, 'one': 1, 'two': 1, 'three': 1}
    assert task_func(input_text) == expected_output