import random

import pytest
from src_0099 import task_func


def test_task_func_single_string():
    num_strings = 1
    string_length = 5
    result = task_func(num_strings, string_length)
    assert len(result) <= string_length
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

def test_task_func_multiple_strings():
    num_strings = 3
    string_length = 10
    result = task_func(num_strings, string_length)
    assert len(result) <= 26
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

def test_task_func_no_strings():
    num_strings = 0
    string_length = 5
    result = task_func(num_strings, string_length)
    assert result == []

def test_task_func_long_strings():
    num_strings = 5
    string_length = 100
    result = task_func(num_strings, string_length)
    assert len(result) <= 26
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

def test_task_func_single_character():
    num_strings = 1
    string_length = 1
    result = task_func(num_strings, string_length)
    assert len(result) == 1
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

def test_task_func_all_same_characters():
    num_strings = 5
    string_length = 10
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(random, 'choices', lambda population, k: ['a'] * k)
        result = task_func(num_strings, string_length)
    assert result == [('a', 50)]

def test_task_func_uniform_distribution():
    num_strings = 26
    string_length = 10
    result = task_func(num_strings, string_length)
    assert len(result) == 26
    assert all(count == 10 for _, count in result)