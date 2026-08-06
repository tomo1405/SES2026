import math

from src_0832 import task_func


def test_task_func_default_values():
    result = list(task_func())
    assert len(result) == 10
    for x, y, distance in result:
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(distance, float)
        assert 1 <= x <= 100
        assert 1 <= y <= 100
        assert distance == math.sqrt(abs(x - y))

def test_task_func_custom_range_and_pairs_count():
    result = list(task_func(range_start=50, range_end=60, pairs_count=5))
    assert len(result) == 5
    for x, y, distance in result:
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(distance, float)
        assert 50 <= x <= 60
        assert 50 <= y <= 60
        assert distance == math.sqrt(abs(x - y))

def test_task_func_with_random_seed():
    seed = 42
    result1 = list(task_func(random_seed=seed))
    result2 = list(task_func(random_seed=seed))
    assert result1 == result2

def test_task_func_edge_cases():
    result = list(task_func(range_start=1, range_end=1, pairs_count=1))
    x, y, distance = result[0]
    assert x == 1
    assert y == 1
    assert distance == 0.0

    result = list(task_func(range_start=-10, range_end=10, pairs_count=1))
    x, y, distance = result[0]
    assert -10 <= x <= 10
    assert -10 <= y <= 10
    assert isinstance(distance, float)