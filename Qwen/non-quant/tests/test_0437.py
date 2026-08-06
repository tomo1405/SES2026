import string

import pytest
from src_0437 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
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
    letter_counts, ax = task_func("abcabc")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['a'] = 2
    expected_counts['b'] = 2
    expected_counts['c'] = 2
    assert letter_counts == expected_counts

def test_task_func_case_insensitivity():
    letter_counts, ax = task_func("ABCabc")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['a'] = 2
    expected_counts['b'] = 2
    expected_counts['c'] = 2
    assert letter_counts == expected_counts

def test_task_func_non_alphabetic_characters():
    letter_counts, ax = task_func("123!@#abc")
    expected_counts = {letter: 0 for letter in string.ascii_lowercase}
    expected_counts['a'] = 1
    expected_counts['b'] = 1
    expected_counts['c'] = 1
    assert letter_counts == expected_counts