import pytest
from src_0832 import task_func
import random
import math

def test_task_func():
    random.seed(42)
    pairs = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]
    expected_output = ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)
    actual_output = task_func(range_start=1, range_end=100, pairs_count=10, random_seed=42)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(range_start=100, range_end=1, pairs_count=10, random_seed=42)