import pytest
from src_0807 import task_func
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def test_task_func_basic():
    text = "This is a simple test."
    result = task_func(text, n=2)
    expected = Counter([("this", "simple"), ("simple", "test")])
    assert result == expected

def test_task_func_no_punctuation():
    text = "Hello, world!"
    result = task_func(text, n=2)
    expected = Counter([("hello", "world")])
    assert result == expected

def test_task_func_single_word():
    text = "Python"
    result = task_func(text, n=2)
    expected = Counter()
    assert result == expected

def test_task_func_stopwords_only():
    text = "and the of in to a"
    result = task_func(text, n=2)
    expected = Counter()
    assert result == expected

def test_task_func_empty_string():
    text = ""
    result = task_func(text, n=2)
    expected = Counter()
    assert result == expected

def test_task_func_large_n():
    text = "This is a test for large n-grams"
    result = task_func(text, n=4)
    expected = Counter([("this", "is", "a", "test"), ("is", "a", "test", "for"), ("a", "test", "for", "large"), ("test", "for", "large", "ngrams")])
    assert result == expected

def test_task_func_case_insensitivity():
    text = "HELLO world HELLO"
    result = task_func(text, n=2)
    expected = Counter([("hello", "world"), ("world", "hello")])
    assert result == expected