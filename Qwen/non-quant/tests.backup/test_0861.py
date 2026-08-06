import pytest
from src_0861 import task_func

def test_task_func_with_no_matches():
    pattern = r'\d{3}'
    result = task_func(5, pattern)
    assert result == []

def test_task_func_with_exact_match():
    pattern = r'abc'
    result = task_func(3, pattern, seed=42)
    assert result == ['abc']

def test_task_func_with_multiple_matches():
    pattern = r'[a-z]'
    result = task_func(10, pattern, seed=42)
    assert len(result) > 1

def test_task_func_with_no_seed():
    pattern = r'[0-9]'
    result1 = task_func(5, pattern)
    result2 = task_func(5, pattern)
    assert result1 != result2

def test_task_func_with_fixed_seed():
    pattern = r'[0-9]'
    result1 = task_func(5, pattern, seed=42)
    result2 = task_func(5, pattern, seed=42)
    assert result1 == result2

def test_task_func_with_special_characters():
    pattern = r'[!@#]'
    result = task_func(10, pattern, seed=42)
    assert result == []