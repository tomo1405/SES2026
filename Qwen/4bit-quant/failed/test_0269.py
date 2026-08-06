import pytest
from src_0269 import task_func

def test_task_func_with_zero_keys():
    result = task_func(0, 5)
    assert result == {}

def test_task_func_with_zero_values():
    result = task_func(5, 0)
    assert result == {}

def test_task_func_with_one_key_and_value():
    result = task_func(1, 1)
    assert list(result.keys()) == ['a'] and list(result.values()) == [1]

def test_task_func_with_multiple_keys_and_values():
    result = task_func(5, 5)
    assert len(result) == 5
    assert all(k in LETTERS for k in result.keys())
    assert list(result.values()) == list(range(1, 6))

def test_task_func_with_more_keys_than_values():
    result = task_func(10, 5)
    assert len(result) == 5
    assert all(k in LETTERS for k in result.keys())
    assert list(result.values()) == list(range(1, 6))

def test_task_func_with_more_values_than_keys():
    result = task_func(5, 10)
    assert len(result) == 5
    assert all(k in LETTERS for k in result.keys())
    assert list(result.values()) == list(range(1, 6))

def test_task_func_with_repeated_keys():
    # Since keys are randomly chosen, we cannot predict exact repetition,
    # but we can check that the length of the dictionary is equal to the number of unique keys.
    result = task_func(10, 5)
    assert len(result) == len(set(result.keys()))