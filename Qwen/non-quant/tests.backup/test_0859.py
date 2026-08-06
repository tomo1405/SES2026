import pytest
from src_0859 import task_func
from collections import Counter

def test_task_func_output_type():
    result = task_func(10)
    assert isinstance(result, Counter)

def test_task_func_output_length():
    n = 20
    result = task_func(n)
    assert sum(result.values()) == n

def test_task_func_with_seed():
    seed = 42
    result1 = task_func(10, seed=seed)
    result2 = task_func(10, seed=seed)
    assert result1 == result2

def test_task_func_no_seed():
    result1 = task_func(10)
    result2 = task_func(10)
    assert result1 != result2

def test_task_func_zero_length():
    result = task_func(0)
    assert result == Counter()

def test_task_func_large_n():
    n = 1000
    result = task_func(n)
    assert sum(result.values()) == n