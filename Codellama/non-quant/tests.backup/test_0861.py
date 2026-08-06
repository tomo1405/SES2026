import pytest
from src_0861 import task_func

def test_task_func_n_positive():
    n = 10
    pattern = r'[a-zA-Z0-9]+'
    seed = 1234
    matches = task_func(n, pattern, seed)
    assert len(matches) == n

def test_task_func_n_negative():
    n = -10
    pattern = r'[a-zA-Z0-9]+'
    seed = 1234
    matches = task_func(n, pattern, seed)
    assert len(matches) == 0

def test_task_func_pattern_positive():
    n = 10
    pattern = r'[a-zA-Z0-9]+'
    seed = 1234
    matches = task_func(n, pattern, seed)
    assert all(re.match(pattern, match) for match in matches)

def test_task_func_pattern_negative():
    n = 10
    pattern = r'[a-zA-Z0-9]+'
    seed = 1234
    matches = task_func(n, pattern, seed)
    assert not any(re.match(r'[a-zA-Z]+', match) for match in matches)

def test_task_func_seed_positive():
    n = 10
    pattern = r'[a-zA-Z0-9]+'
    seed = 1234
    matches1 = task_func(n, pattern, seed)
    matches2 = task_func(n, pattern, seed)
    assert matches1 == matches2

def test_task_func_seed_negative():
    n = 10
    pattern = r'[a-zA-Z0-9]+'
    seed1 = 1234
    seed2 = 5678
    matches1 = task_func(n, pattern, seed1)
    matches2 = task_func(n, pattern, seed2)
    assert matches1 != matches2