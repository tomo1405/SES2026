import pytest
from src_0333 import task_func
from collections import Counter
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
import nltk
nltk.download('stopwords')

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_no_non_stopwords():
    text = "and but for if in of on that the to"
    assert task_func(text) == {}

def test_task_func_single_word():
    text = "hello"
    assert task_func(text) == {'hello': 1}

def test_task_func_multiple_words():
    text = "hello world hello"
    assert task_func(text) == {'world': 1, 'hello': 2}

def test_task_func_case_insensitivity():
    text = "Hello hello HELLO"
    assert task_func(text) == {'hello': 3}

def test_task_func_with_punctuation():
    text = "Hello, world! Hello."
    assert task_func(text) == {'world': 1, 'hello': 2}

def test_task_func_with_numbers():
    text = "Hello 123 world 456 hello"
    assert task_func(text) == {'world': 1, 'hello': 2}