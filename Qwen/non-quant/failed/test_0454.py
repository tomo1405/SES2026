import pytest
from src_0454 import task_func

def test_task_func_length():
    n = 10
    pattern = r'^[a-zA-Z]{10}$'
    result = task_func(n, pattern)
    assert len(result) == n

def test_task_func_pattern_match():
    n = 5
    pattern = r'^[A-Z]+$'
    result = task_func(n, pattern)
    assert re.match(pattern, result)

def test_task_func_lowercase_only():
    n = 8
    pattern = r'^[a-z]+$'
    result = task_func(n, pattern)
    assert re.match(pattern, result)

def test_task_func_mixed_case():
    n = 12
    pattern = r'^[a-zA-Z]+$'
    result = task_func(n, pattern)
    assert re.match(pattern, result)

def test_task_func_empty_string():
    n = 0
    pattern = r'^$'
    result = task_func(n, pattern)
    assert result == ''

def test_task_func_special_characters():
    n = 7
    pattern = r'^[^a-zA-Z]+$'  # This pattern should never match any generated string
    with pytest.raises(AssertionError):
        result = task_func(n, pattern)
        assert re.match(pattern, result)