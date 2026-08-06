import random
import math
from src_0832 import task_func
import pytest

def test_task_func_default_args():
    result = task_func()
    assert isinstance(result, tuple)
    for x, y, z in result:
        assert isinstance(x, int) and 1 <= x <= 100
        assert isinstance(y, int) and 1 <= y <= 100
        assert isinstance(z, float) and 0 <= z <= 100

def test_task_func_custom_args():
    range_start = 10
    range_end = 100
    pairs_count = 5
    random_seed = 42
    random.seed(random_seed)
    expected_result = [
        (random.randint(range_start, range_end), random.randint(range_start, range_end), math.sqrt(abs(x - y)))
        for x, y in [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    ]
    result = task_func(range_start, range_end, pairs_count, random_seed)
    assert isinstance(result, tuple)
    assert list(result) == expected_result

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func(-1, 100, 10, None)
    with pytest.raises(ValueError):
        task_func(1, -100, 10, None)
    with pytest.raises(ValueError):
        task_func(1, 100, -10, None)