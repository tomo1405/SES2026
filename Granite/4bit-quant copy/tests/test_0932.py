import pytest
from collections import defaultdict
import re

def task_func(word: str) -> dict:
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    return occurrences

def test_task_func():
    word = "Hello, World!"
    expected_result = {'He': 1, 'el': 1, 'll': 2, 'o,': 1, 'o ': 1, ' W': 1, 'or': 1, 'ld': 1, '!': 1}
    assert task_func(word) == expected_result

def test_task_func_empty_string():
    word = ""
    expected_result = {}
    assert task_func(word) == expected_result

def test_task_func_no_alphabetic_characters():
    word = "12345"
    expected_result = {}
    assert task_func(word) == expected_result

def test_task_func_single_character():
    word = "A"
    expected_result = {}
    assert task_func(word) == expected_result