import re
import random
from nltk.corpus import words
from random import sample
import nltk
nltk.download('words')
SAMPLE_ENGLISH_WORDS = set(words.words())
def task_func(s, n):
    word_list = re.findall(r'\b\w+\b', s.lower())
    english_words = [word for word in word_list if word in SAMPLE_ENGLISH_WORDS]
    if len(english_words) < n:
        return english_words
    else:
        return sample(english_words, n)
import pytest

def test_task_func():
    s = "This is a sample sentence with some English words like cat and dog."
    n = 3
    expected_output = ['cat', 'dog', 'sample']
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_less_english_words():
    s = "This sentence has only two English words."
    n = 5
    expected_output = ['sentence', 'only']
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_no_english_words():
    s = "This sentence has no English words."
    n = 3
    expected_output = []
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_n():
    s = "This is another sample sentence."
    n = -1
    expected_output = []
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"