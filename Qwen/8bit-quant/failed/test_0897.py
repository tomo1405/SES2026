import pytest
from src_0897 import task_func
from collections import Counter

def test_task_func_length_zero():
    result = task_func(0, 5)
    assert result == Counter()

def test_task_func_count_zero():
    result = task_func(3, 0)
    assert result == Counter()

def test_task_func_default_seed():
    result = task_func(3, 5)
    expected = Counter({'a': 4, 'b': 3, 'c': 3, 'd': 2, 'e': 3})
    assert result == expected

def test_task_func_custom_seed():
    result = task_func(3, 5, seed=123)
    expected = Counter({'a': 4, 'b': 3, 'c': 3, 'd': 2, 'e': 3})
    assert result == expected

def test_task_func_single_string():
    result = task_func(3, 1)
    assert len(result) <= 3

def test_task_func_multiple_strings():
    result = task_func(3, 10)
    assert sum(result.values()) == 30

def test_task_func_all_a():
    result = task_func(3, 5, seed=456)
    assert result == Counter({'a': 15})

def test_task_func_all_e():
    result = task_func(3, 5, seed=789)
    assert result == Counter({'e': 15})