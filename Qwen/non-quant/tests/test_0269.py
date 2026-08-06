import random

import pytest
from src_0269 import task_func


def test_task_func_with_zero_keys():
    result = task_func(0, 5)
    assert result == {}

def test_task_func_with_zero_values():
    result = task_func(5, 0)
    assert result == {}

def test_task_func_with_negative_keys():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_with_negative_values():
    with pytest.raises(ValueError):
        task_func(5, -1)

def test_task_func_with_positive_keys_and_values():
    result = task_func(5, 5)
    assert len(result) == 5
    assert all(isinstance(k, str) and k in LETTERS for k in result.keys())
    assert all(isinstance(v, list) and v == list(range(1, 6)) for v in result.values())

def test_task_func_with_more_keys_than_values():
    result = task_func(10, 5)
    assert len(result) == 5
    assert all(isinstance(k, str) and k in LETTERS for k in result.keys())
    assert all(isinstance(v, list) and v == list(range(1, 6)) for v in result.values())

def test_task_func_with_fewer_keys_than_values():
    result = task_func(3, 5)
    assert len(result) == 3
    assert all(isinstance(k, str) and k in LETTERS for k in result.keys())
    assert all(isinstance(v, list) and v == list(range(1, 6)) for v in result.values())

def test_task_func_deterministic_keys():
    random.seed(42)
    result1 = task_func(5, 5)
    random.seed(42)
    result2 = task_func(5, 5)
    assert result1 == result2