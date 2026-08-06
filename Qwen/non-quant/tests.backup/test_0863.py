import pytest
from src_0863 import task_func

def test_task_func_with_seed():
    n = 10
    seed = 42
    result = task_func(n, seed)
    expected = {
        'a': ['a', 'a'],
        'c': ['c', 'c'],
        'd': ['d'],
        'e': ['e', 'e'],
        'g': ['g'],
        'h': ['h'],
        'i': ['i'],
        'k': ['k'],
        'l': ['l'],
        'm': ['m']
    }
    assert result == expected

def test_task_func_without_seed():
    n = 5
    result = task_func(n)
    assert all(isinstance(value, list) for value in result.values())
    assert sum(len(value) for value in result.values()) == n

def test_task_func_with_zero_n():
    n = 0
    result = task_func(n)
    assert result == defaultdict(list)

def test_task_func_with_large_n():
    n = 1000
    seed = 42
    result = task_func(n, seed)
    assert sum(len(value) for value in result.values()) == n