import pytest
from src_0269 import task_func

def test_task_func_returns_dict():
    n_keys = 5
    n_values = 10
    result = task_func(n_keys, n_values)
    assert isinstance(result, dict)

def test_task_func_returns_ordered_dict():
    n_keys = 5
    n_values = 10
    result = task_func(n_keys, n_values)
    assert isinstance(result, collections.OrderedDict)

def test_task_func_returns_dict_with_correct_keys():
    n_keys = 5
    n_values = 10
    result = task_func(n_keys, n_values)
    assert set(result.keys()) == set(LETTERS[:n_keys])

def test_task_func_returns_dict_with_correct_values():
    n_keys = 5
    n_values = 10
    result = task_func(n_keys, n_values)
    assert all(result[k] == list(range(1, n_values + 1)) for k in result.keys())