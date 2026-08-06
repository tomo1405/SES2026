import pytest
from src_0727 import task_func
import random
from nltk.corpus import words
from random import sample

# Ensure the words corpus is downloaded
import nltk
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())

# Mocking the random.sample function to control its behavior in tests
def mock_sample(population, k):
    return population[:k]

random.sample = mock_sample

def test_task_func_no_english_words():
    input_string = "12345!@#$%"
    n = 3
    result = task_func(input_string, n)
    assert result == []

def test_task_func_fewer_than_n_english_words():
    input_string = "hello world"
    n = 5
    result = task_func(input_string, n)
    assert result == ['hello', 'world']

def test_task_func_more_than_n_english_words():
    input_string = "hello world this is a test"
    n = 2
    result = task_func(input_string, n)
    assert result == ['hello', 'world']  # Since we mocked sample, it returns the first n elements

def test_task_func_exact_n_english_words():
    input_string = "hello world"
    n = 2
    result = task_func(input_string, n)
    assert result == ['hello', 'world']

def test_task_func_empty_string():
    input_string = ""
    n = 3
    result = task_func(input_string, n)
    assert result == []

def test_task_func_punctuation():
    input_string = "Hello, world! This is a test."
    n = 3
    result = task_func(input_string, n)
    assert result == ['hello', 'world', 'this']