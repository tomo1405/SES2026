import pytest
from src_0900 import task_func
import numpy as np

def test_task_func_length():
    result = task_func(length=10)
    assert len(result) == 11  # Starts at 0, so length is +1

def test_task_func_default_length():
    result = task_func()
    assert len(result) == 10001  # Default length is 10000, starts at 0

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_seed_reproducibility():
    result1 = task_func(seed=42)
    result2 = task_func(seed=42)
    assert np.array_equal(result1, result2)

def test_task_func_random_steps():
    result = task_func(seed=42)
    assert all(step in [-1, 1] for step in result[1:])  # Exclude the initial 0

def test_task_func_cumulative_sum():
    result = task_func(length=5, seed=42)
    expected = np.cumsum([0, 1, -1, 1, -1, 1])
    assert np.array_equal(result, expected)