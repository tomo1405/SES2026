import pytest
from src_0861 import task_func

def test_task_func_with_fixed_seed():
    n = 10
    pattern = r'\d'
    seed = 42
    expected_matches = ['5', '8', '3']
    assert task_func(n, pattern, seed) == expected_matches

def test_task_func_with_no_seed():
    n = 10
    pattern = r'[A-Z]'
    # Since no seed is provided, the result can vary
    # We can only check if the output is a list of strings that match the pattern
    matches = task_func(n, pattern)
    assert isinstance(matches, list)
    for match in matches:
        assert isinstance(match, str)
        assert re.match(pattern, match)

def test_task_func_with_empty_pattern():
    n = 10
    pattern = ''
    seed = 42
    matches = task_func(n, pattern, seed)
    assert matches == []

def test_task_func_with_non_matching_pattern():
    n = 10
    pattern = r'[a-z]{10}'
    seed = 42
    matches = task_func(n, pattern, seed)
    assert matches == []

def test_task_func_with_large_n():
    n = 100
    pattern = r'\d'
    seed = 42
    matches = task_func(n, pattern, seed)
    assert len(matches) <= n
    for match in matches:
        assert match.isdigit()

def test_task_func_with_zero_n():
    n = 0
    pattern = r'\d'
    seed = 42
    matches = task_func(n, pattern, seed)
    assert matches == []