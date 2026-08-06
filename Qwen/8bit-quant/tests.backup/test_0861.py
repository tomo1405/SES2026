import pytest
from src_0861 import task_func

def test_task_func_with_no_matches():
    # Test with a pattern that will not match any generated string
    n = 10
    pattern = r'z{5}'  # Pattern for exactly 5 'z's which is unlikely to appear
    seed = 42
    result = task_func(n, pattern, seed)
    assert result == []

def test_task_func_with_fixed_seed_and_pattern():
    # Test with a fixed seed and a pattern that should match
    n = 20
    pattern = r'[A-Z]{2}'  # Pattern for exactly 2 uppercase letters
    seed = 42
    result = task_func(n, pattern, seed)
    expected_matches = ['JH', 'WU', 'VQ']
    assert result == expected_matches

def test_task_func_without_seed():
    # Test without providing a seed, which should produce different results on each run
    n = 10
    pattern = r'\d'  # Pattern for any digit
    result1 = task_func(n, pattern)
    result2 = task_func(n, pattern)
    assert result1 != result2  # Results should be different due to lack of seed

def test_task_func_with_long_string():
    # Test with a longer string
    n = 100
    pattern = r'\w{3}'  # Pattern for any word character repeated 3 times
    seed = 42
    result = task_func(n, pattern, seed)
    assert len(result) > 0  # There should be at least one match

def test_task_func_with_special_characters():
    # Test with a pattern including special characters
    n = 20
    pattern = r'[^a-zA-Z0-9]'  # Pattern for any non-alphanumeric character
    seed = 42
    result = task_func(n, pattern, seed)
    assert len(result) > 0  # There should be at least one match

def test_task_func_with_empty_pattern():
    # Test with an empty pattern, which should match the entire string
    n = 10
    pattern = r''  # Empty pattern
    seed = 42
    result = task_func(n, pattern, seed)
    assert len(result) == n  # Each character should be matched individually

def test_task_func_with_non_matching_pattern():
    # Test with a pattern that cannot possibly match the generated string
    n = 10
    pattern = r'x{100}'  # Pattern for exactly 100 'x's which is unlikely to appear
    seed = 42
    result = task_func(n, pattern, seed)
    assert result == []