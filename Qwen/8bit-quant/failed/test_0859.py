import pytest
from src_0859 import task_func
from collections import Counter

def test_task_func_with_seed():
    n = 10
    seed = 42
    result = task_func(n, seed)
    expected = Counter({'l': 3, 'x': 2, 'f': 2, 'j': 1, 'v': 1, 'm': 1})
    assert result == expected

def test_task_func_without_seed():
    n = 10
    result = task_func(n)
    assert len(result) <= n
    assert all(isinstance(count, int) and count >= 0 for count in result.values())

def test_task_func_with_zero_n():
    n = 0
    result = task_func(n)
    assert result == Counter()

def test_task_func_with_large_n():
    n = 1000
    result = task_func(n)
    assert len(result) <= n
    assert sum(result.values()) == n
    assert all(isinstance(count, int) and count >= 0 for count in result.values())