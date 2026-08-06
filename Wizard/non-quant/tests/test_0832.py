python
import random
import math
import pytest

def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    random.seed(random_seed)
    pairs = [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    return ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)

def test_task_func():
    # Test default values
    result = list(task_func())
    assert len(result) == 10
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result)
    assert all(isinstance(x[0], int) and isinstance(x[1], int) and isinstance(x[2], float) for x in result)

    # Test custom values
    result = list(task_func(range_start=0, range_end=10, pairs_count=5, random_seed=42))
    assert len(result) == 5
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result)
    assert all(isinstance(x[0], int) and isinstance(x[1], int) and isinstance(x[2], float) for x in result)
    assert all(x[0] >= 0 and x[0] <= 10 and x[1] >= 0 and x[1] <= 10 for x in result)
    assert all(x[2] >= 0 and x[2] <= 10 for x in result)