python
import re
import random
import pytest
from nltk.corpus import words
from random import sample

# Ensure the words corpus is downloaded
import nltk
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())

def task_func(s, n):

    word_list = re.findall(r'\b\w+\b', s.lower())  # Convert to lowercase for comparison
    english_words = [word for word in word_list if word in SAMPLE_ENGLISH_WORDS]
    if len(english_words) < n:
        return english_words
    else:
        return sample(english_words, n)

# Test cases
def test_task_func_valid_input():
    assert task_func('The quick brown fox jumps over the lazy dog', 5) == ['quick', 'brown', 'fox', 'jumps', 'lazy']

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('The quick brown fox jumps over the lazy dog', 10)

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func('', 5)

def test_task_func_non_string_input():
    with pytest.raises(TypeError):
        task_func(123, 5)

def test_task_func_non_integer_input():
    with pytest.raises(TypeError):
        task_func('The quick brown fox jumps over the lazy dog', '5')