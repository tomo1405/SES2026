import pytest
from src_0832 import task_func

def test_task_func_default_values():
    result = list(task_func())
    assert len(result) == 10
    for x, y, distance in result:
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(distance, float)

def test_task_func_custom_range():
    result = list(task_func(range_start=50, range_end=150))
    for x, y, distance in result:
        assert 50 <= x <= 150
        assert 50 <= y <= 150

def test_task_func_custom_pairs_count():
    result = list(task_func(pairs_count=5))
    assert len(result) == 5

def test_task_func_random_seed():
    seed = 42
    result1 = list(task_func(random_seed=seed))
    result2 = list(task_func(random_seed=seed))
    assert result1 == result2

def test_task_func_distance_calculation():
    result = list(task_func(range_start=0, range_end=0, pairs_count=1))
    x, y, distance = result[0]
    assert x == 0
    assert y == 0
    assert distance == 0.0

def test_task_func_negative_range():
    result = list(task_func(range_start=-10, range_end=10))
    for x, y, distance in result:
        assert -10 <= x <= 10
        assert -10 <= y <= 10