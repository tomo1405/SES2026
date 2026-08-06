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
    word = "Hello World"
    expected_result = {'He': 1, 'el': 1, 'll': 2, 'o ': 1, 'oW': 1, ' Wo': 1, 'or': 1, 'rl': 1, 'ld': 1}
    result = task_func(word)
    assert result == expected_result

def test_task_func_with_special_characters():
    word = "Hello!@# World$%^"
    expected_result = {'He': 1, 'el': 1, 'll': 2, 'o!': 1, 'o#': 1, ' Wo': 1, 'or': 1, 'rl': 1, 'ld': 1, 'd$': 1, 'd^': 1}
    result = task_func(word)
    assert result == expected_result