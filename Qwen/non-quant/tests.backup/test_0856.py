import pytest
from src_0856 import task_func
import string
import collections

def test_task_func_output_type():
    result = task_func(1, 1)
    assert isinstance(result, dict)

def test_task_func_character_counts():
    n_strings = 3
    string_length = 4
    result = task_func(n_strings, string_length)
    total_characters = n_strings * string_length
    assert sum(result.values()) == total_characters

def test_task_func_valid_characters():
    n_strings = 1
    string_length = 10
    result = task_func(n_strings, string_length)
    all_characters = ''.join(result.keys())
    for char in all_characters:
        assert char in string.ascii_letters + string.digits

def test_task_func_empty_string():
    result = task_func(0, 10)
    assert result == {}

def test_task_func_single_character():
    result = task_func(1, 1)
    assert len(result) <= 1

def test_task_func_large_input():
    n_strings = 1000
    string_length = 1000
    result = task_func(n_strings, string_length)
    total_characters = n_strings * string_length
    assert sum(result.values()) == total_characters