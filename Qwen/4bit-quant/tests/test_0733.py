import pytest
from src_0733 import task_func
from nltk.stem import PorterStemmer
from collections import Counter

# Ensure the NLTK data is downloaded
import nltk
nltk.download('punkt')

def test_task_func_with_empty_string():
    assert task_func("") == {}

def test_task_func_with_single_word():
    assert task_func("Hello") == {'hello': 1}

def test_task_func_with_multiple_words():
    assert task_func("Hello world! Hello, everyone.") == {'hello': 2, 'world': 1, 'everyon': 1}

def test_task_func_with_punctuation():
    assert task_func("!!!Hello... World?") == {'hello': 1, 'world': 1}

def test_task_func_with_numbers():
    assert task_func("Hello 123 world!") == {'hello': 1, 'world': 1}

def test_task_func_with_special_characters():
    assert task_func("$$$Hello%%% world!") == {'hello': 1, 'world': 1}

def test_task_func_with_stemming():
    assert task_func("Running runs ran") == {'run': 3}

def test_task_func_with_case_insensitivity():
    assert task_func("Hello hello HELLO") == {'hello': 3}

def test_task_func_with_large_input():
    large_input = " ".join(["This is a test"] * 100)
    expected_output = {'this': 100, 'is': 100, 'a': 100, 'test': 100}
    assert task_func(large_input) == expected_output

def test_task_func_with_no_words():
    assert task_func("!@#$%^&*()") == {}

def test_task_func_with_whitespace():
    assert task_func("   ") == {}