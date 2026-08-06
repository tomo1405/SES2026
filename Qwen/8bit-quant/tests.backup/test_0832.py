import pytest
from src_0832 import task_func

def test_task_func_default_parameters():
    result = list(task_func())
    assert len(result) == 10
    for x, y, distance in result:
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(distance, float)
        assert distance >= 0

def test_task_func_custom_range_and_pairs_count():
    result = list(task_func(range_start=50, range_end=60, pairs_count=5))
    assert len(result) == 5
    for x, y, distance in result:
        assert 50 <= x <= 60
        assert 50 <= y <= 60
        assert isinstance(distance, float)
        assert distance >= 0

def test_task_func_with_random_seed():
    seed = 42
    result1 = list(task_func(random_seed=seed))
    result2 = list(task_func(random_seed=seed))
    assert result1 == result2

def test_task_func_distance_calculation():
    result = list(task_func(range_start=0, range_end=0, pairs_count=1))
    assert result == [(0, 0, 0.0)]

def test_task_func_large_range():
    result = list(task_func(range_start=-1000, range_end=1000, pairs_count=1))
    x, y, distance = result[0]
    assert -1000 <= x <= 1000
    assert -1000 <= y <= 1000
    assert isinstance(distance, float)
    assert distance >= 0