import pytest
from src_0861 import task_func

def test_task_func_returns_list():
    n = 10
    pattern = r'\d+'
    seed = 1234
    result = task_func(n, pattern, seed)
    assert isinstance(result, list)

def test_task_func_returns_correct_matches():
    n = 10
    pattern = r'\d+'
    seed = 1234
    result = task_func(n, pattern, seed)
    assert result == ['1', '2', '3', '4']

def test_task_func_returns_correct_matches_with_different_seed():
    n = 10
    pattern = r'\d+'
    seed = 5678
    result = task_func(n, pattern, seed)
    assert result == ['5', '6', '7', '8']

def test_task_func_returns_correct_matches_with_different_pattern():
    n = 10
    pattern = r'[a-zA-Z]+'
    seed = 1234
    result = task_func(n, pattern, seed)
    assert result == ['a', 'b', 'c', 'd']

def test_task_func_returns_correct_matches_with_different_n():
    n = 5
    pattern = r'\d+'
    seed = 1234
    result = task_func(n, pattern, seed)
    assert result == ['1', '2', '3', '4']