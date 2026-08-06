python
import random
import math
import pytest

def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    random.seed(random_seed)
    pairs = [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    return ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)

def test_task_func():
    pairs = list(task_func(pairs_count=5))
    assert len(pairs) == 5
    assert all(isinstance(pair, tuple) and len(pair) == 3 for pair in pairs)
    assert all(isinstance(pair[0], int) and isinstance(pair[1], int) and isinstance(pair[2], float) for pair in pairs)
    assert all(pair[0] != pair[1] for pair in pairs)
    assert all(pair[2] >= 0 for pair in pairs)