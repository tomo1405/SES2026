import pytest
from src_0856 import task_func

def test_task_func_returns_dict():
    n_strings = 10
    string_length = 10
    result = task_func(n_strings, string_length)
    assert isinstance(result, dict)

def test_task_func_returns_dict_with_correct_keys():
    n_strings = 10
    string_length = 10
    result = task_func(n_strings, string_length)
    assert set(result.keys()) == set(VALID_CHARACTERS)

def test_task_func_returns_dict_with_correct_values():
    n_strings = 10
    string_length = 10
    result = task_func(n_strings, string_length)
    for key, value in result.items():
        assert isinstance(key, str)
        assert isinstance(value, int)
        assert value >= 0