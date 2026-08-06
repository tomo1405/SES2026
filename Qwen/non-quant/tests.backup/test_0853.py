import pytest
from src_0853 import task_func

def test_task_func_negative_max_length():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_zero_max_length():
    with pytest.raises(ValueError):
        task_func(0, 5)

def test_task_func_min_max_length():
    result = task_func(1, 5, seed=42)
    assert len(result) == 5
    for item in result:
        assert len(item) == 1
        assert item in string.ascii_lowercase

def test_task_func_max_max_length():
    result = task_func(26, 5, seed=42)
    assert len(result) == 5
    for item in result:
        assert 1 <= len(item) <= 26
        assert all(char in string.ascii_lowercase for char in item)

def test_task_func_reproducibility():
    result1 = task_func(10, 5, seed=42)
    result2 = task_func(10, 5, seed=42)
    assert result1 == result2

def test_task_func_no_seed():
    result1 = task_func(10, 5)
    result2 = task_func(10, 5)
    assert result1 != result2

def test_task_func_single_sample():
    result = task_func(10, 1, seed=42)
    assert len(result) == 1
    assert 1 <= len(result[0]) <= 10
    assert all(char in string.ascii_lowercase for char in result[0])