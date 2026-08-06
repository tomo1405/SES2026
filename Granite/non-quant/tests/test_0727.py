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
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization

def test_task_func():
    s = "This is a sample sentence with some English words like apple and orange."
    n = 3
    expected_output = ['apple', 'orange', 'sample']
    random.seed(0)  # Set random seed for reproducibility
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_less_english_words():
    s = "This sentence has only two English words: cat and dog."
    n = 3
    expected_output = ['cat', 'dog']
    random.seed(0)  # Set random seed for reproducibility
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_no_english_words():
    s = "This sentence has no English words."
    n = 3
    expected_output = []
    random.seed(0)  # Set random seed for reproducibility
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_n():
    s = "This sentence has some English words like apple and orange."
    n = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(s, n)
    assert "n must be a positive integer" in str(excinfo.value), "Expected ValueError not raised"