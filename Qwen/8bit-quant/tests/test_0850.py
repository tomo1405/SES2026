import pytest
from src_0850 import task_func
from collections import Counter
from nltk.corpus import stopwords

# Mocking the stopwords to avoid downloading the NLTK data
STOPWORDS = set(stopwords.words('english'))

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_single_word():
    result = task_func("hello")
    assert result == {'hello': 1}

def test_task_func_multiple_words():
    result = task_func("hello world hello")
    assert result == {'hello': 2, 'world': 1}

def test_task_func_with_stopwords():
    result = task_func("this is a test")
    assert result == {'test': 1}

def test_task_func_with_punctuation():
    result = task_func("hello, world!")
    assert result == {'hello': 1, 'world': 1}

def test_task_func_multiple_lines():
    result = task_func("hello world\nhello again")
    assert result == {'hello': 2, 'world': 1, 'again': 1}

def test_task_func_case_insensitivity():
    result = task_func("Hello hello HELLO")
    assert result == {'hello': 3}