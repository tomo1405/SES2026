import pytest
from src_0853 import task_func

def test_task_func_negative_max_length():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_zero_max_length():
    with pytest.raises(ValueError):
        task_func(0, 5)

def test_task_func_positive_max_length():
    result = task_func(5, 3)
    assert len(result) == 3
    for item in result:
        assert 1 <= len(item) <= 5
        assert all(c in string.ascii_lowercase for c in item)

def test_task_func_with_seed():
    seed_value = 42
    result1 = task_func(5, 3, seed=seed_value)
    result2 = task_func(5, 3, seed=seed_value)
    assert result1 == result2

def test_task_func_no_seed():
    result1 = task_func(5, 3)
    result2 = task_func(5, 3)
    assert result1 != result2

def test_task_func_single_sample():
    result = task_func(5, 1)
    assert len(result) == 1
    assert 1 <= len(result[0]) <= 5
    assert all(c in string.ascii_lowercase for c in result[0])

def test_task_func_max_length_one():
    result = task_func(1, 3)
    assert len(result) == 3
    for item in result:
        assert len(item) == 1
        assert item in string.ascii_lowercase