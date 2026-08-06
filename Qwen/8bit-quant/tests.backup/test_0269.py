import pytest
from src_0269 import task_func

def test_task_func_with_zero_keys():
    result = task_func(0, 5)
    assert result == {}

def test_task_func_with_zero_values():
    result = task_func(5, 0)
    assert result == {}

def test_task_func_with_positive_keys_and_values():
    result = task_func(3, 3)
    assert len(result) == 3
    assert all(isinstance(k, str) and k in 'abcdefghij' for k in result.keys())
    assert all(isinstance(v, list) and v == [1, 2, 3] for v in result.values())

def test_task_func_with_more_keys_than_values():
    result = task_func(5, 3)
    assert len(result) == 5
    assert all(isinstance(k, str) and k in 'abcdefghij' for k in result.keys())
    assert all(isinstance(v, list) and v == [1, 2, 3] for v in result.values())

def test_task_func_with_more_values_than_keys():
    result = task_func(3, 5)
    assert len(result) == 3
    assert all(isinstance(k, str) and k in 'abcdefghij' for k in result.keys())
    assert all(isinstance(v, list) and v == [1, 2, 3] for v in result.values())

def test_task_func_with_max_keys_and_values():
    result = task_func(10, 10)
    assert len(result) == 10
    assert all(isinstance(k, str) and k in 'abcdefghij' for k in result.keys())
    assert all(isinstance(v, list) and v == list(range(1, 11)) for v in result.values())