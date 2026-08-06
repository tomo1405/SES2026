import pytest
from src_0727 import task_func
import re
import random
from nltk.corpus import words
from random import sample

# Ensure the words corpus is downloaded
import nltk
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())

def test_task_func_no_english_words():
    s = "12345!@#$%"
    n = 3
    result = task_func(s, n)
    assert result == []

def test_task_func_fewer_than_n_english_words():
    s = "hello world"
    n = 5
    result = task_func(s, n)
    assert set(result) == {"hello", "world"}

def test_task_func_exactly_n_english_words():
    s = "hello world"
    n = 2
    result = task_func(s, n)
    assert set(result) == {"hello", "world"}

def test_task_func_more_than_n_english_words():
    s = "hello world this is a test"
    n = 2
    result = task_func(s, n)
    assert len(result) == n
    assert all(word in ["hello", "world", "this", "is", "a", "test"] for word in result)

def test_task_func_random_sampling():
    s = "hello world this is a test"
    n = 2
    result1 = task_func(s, n)
    result2 = task_func(s, n)
    assert len(result1) == n
    assert len(result2) == n
    assert result1 != result2  # Random sampling should give different results

def test_task_func_empty_string():
    s = ""
    n = 3
    result = task_func(s, n)
    assert result == []

def test_task_func_single_word():
    s = "hello"
    n = 1
    result = task_func(s, n)
    assert result == ["hello"]

def test_task_func_single_non_english_word():
    s = "h3ll0"
    n = 1
    result = task_func(s, n)
    assert result == []