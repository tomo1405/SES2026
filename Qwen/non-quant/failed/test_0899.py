import pytest
from src_0899 import task_func
from collections import Counter

def test_task_func_with_zero_count():
    result = task_func(0)
    assert result == Counter()

def test_task_func_with_positive_count():
    result = task_func(5, seed=42)
    expected = Counter([('d', 'e'), ('a', 'b'), ('a', 'd'), ('c', 'c'), ('b', 'c')])
    assert result == expected

def test_task_func_with_large_count():
    result = task_func(100, seed=42)
    expected = Counter([('d', 'e'), ('a', 'b'), ('a', 'd'), ('c', 'c'), ('b', 'c')] * 20)
    assert result == expected

def test_task_func_with_different_seed():
    result1 = task_func(5, seed=123)
    result2 = task_func(5, seed=456)
    assert result1 != result2

def test_task_func_with_single_letter():
    result = task_func(1, seed=42)
    expected = Counter([('d', 'e')])
    assert result == expected