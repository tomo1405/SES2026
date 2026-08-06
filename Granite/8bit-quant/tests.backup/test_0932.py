import pytest
from collections import defaultdict
import re
from src_0932 import task_func

def test_task_func():
    word = "Hello World"
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    assert task_func(word) == occurrences

def test_task_func_empty_string():
    word = ""
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    assert task_func(word) == occurrences

def test_task_func_no_alphabetic_characters():
    word = "12345"
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    assert task_func(word) == occurrences