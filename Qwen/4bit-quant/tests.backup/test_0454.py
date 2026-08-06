import pytest
from src_0454 import task_func

def test_task_func_with_valid_pattern():
    pattern = r'^[a-zA-Z]+$'
    result = task_func(5, pattern)
    assert isinstance(result, str)
    assert len(result) == 5
    assert re.match(pattern, result)

def test_task_func_with_specific_pattern():
    pattern = r'^[A-Z]+$'
    result = task_func(3, pattern)
    assert isinstance(result, str)
    assert len(result) == 3
    assert re.match(pattern, result)

def test_task_func_with_empty_string():
    pattern = r'^$'
    result = task_func(0, pattern)
    assert isinstance(result, str)
    assert len(result) == 0
    assert re.match(pattern, result)

def test_task_func_with_invalid_pattern():
    pattern = r'^\d+$'
    with pytest.raises(AssertionError):
        task_func(5, pattern)

def test_task_func_with_long_pattern():
    pattern = r'^[a-zA-Z]{10}$'
    result = task_func(10, pattern)
    assert isinstance(result, str)
    assert len(result) == 10
    assert re.match(pattern, result)