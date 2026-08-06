import pytest
from src_0454 import task_func
import re

def test_task_func_length():
    n = 5
    pattern = r'^[a-zA-Z]{5}$'
    result = task_func(n, pattern)
    assert len(result) == n

def test_task_func_pattern_match():
    n = 10
    pattern = r'^[a-zA-Z]+$'
    result = task_func(n, pattern)
    assert re.match(pattern, result)

def test_task_func_case_insensitivity():
    n = 7
    pattern = r'^[A-Z]+$'
    result = task_func(n, pattern)
    assert result.isupper()

def test_task_func_randomness():
    n = 8
    pattern = r'^[a-zA-Z]+$'
    result1 = task_func(n, pattern)
    result2 = task_func(n, pattern)
    assert result1 != result2

def test_task_func_empty_pattern():
    n = 3
    pattern = r'^$'
    with pytest.raises(re.error):
        task_func(n, pattern)

def test_task_func_invalid_pattern():
    n = 4
    pattern = r'('
    with pytest.raises(re.error):
        task_func(n, pattern)