import pytest
from src_0856 import task_func
import random
import string
import collections

def test_task_func():
    n_strings = 10
    string_length = 5
    expected_result = collections.Counter(''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(string_length)
        for _ in range(n_strings)
    ))
    actual_result = task_func(n_strings, string_length)
    assert actual_result == expected_result

def test_task_func_with_zero_strings():
    n_strings = 0
    string_length = 5
    expected_result = collections.Counter('')
    actual_result = task_func(n_strings, string_length)
    assert actual_result == expected_result

def test_task_func_with_zero_length():
    n_strings = 10
    string_length = 0
    expected_result = collections.Counter('')
    actual_result = task_func(n_strings, string_length)
    assert actual_result == expected_result

def test_task_func_with_negative_strings():
    n_strings = -10
    string_length = 5
    with pytest.raises(ValueError):
        task_func(n_strings, string_length)

def test_task_func_with_negative_length():
    n_strings = 10
    string_length = -5
    with pytest.raises(ValueError):
        task_func(n_strings, string_length)