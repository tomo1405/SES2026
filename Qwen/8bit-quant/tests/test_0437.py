import string

import pytest
from src_0437 import task_func


def test_task_func_type_error():
    with pytest.raises(TypeError, match="Expected string input"):
        task_func(123)

def test_task_func_empty_string():
    letter_counts, ax = task_func("")
    assert letter_counts == {letter: 0 for letter in string.ascii_lowercase}

def test_task_func_single_letter():
    letter_counts, ax = task_func("a")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['a'] = 1
    assert letter_counts == expected_counts

def test_task_func_multiple_letters():
    letter_counts, ax = task_func("hello world")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['h'] = 1
    expected_counts['e'] = 1
    expected_counts['l'] = 3
    expected_counts['o'] = 2
    expected_counts['w'] = 1
    expected_counts['r'] = 1
    expected_counts['d'] = 1
    assert letter_counts == expected_counts

def test_task_func_case_insensitivity():
    letter_counts, ax = task_func("HELLO WORLD")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['h'] = 1
    expected_counts['e'] = 1
    expected_counts['l'] = 3
    expected_counts['o'] = 2
    expected_counts['w'] = 1
    expected_counts['r'] = 1
    expected_counts['d'] = 1
    assert letter_counts == expected_counts

def test_task_func_non_alphabetic_characters():
    letter_counts, ax = task_func("hello, world!")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['h'] = 1
    expected_counts['e'] = 1
    expected_counts['l'] = 3
    expected_counts['o'] = 2
    expected_counts['w'] = 1
    expected_counts['r'] = 1
    expected_counts['d'] = 1
    assert letter_counts == expected_counts