import pytest
from src_0900 import task_func
import numpy as np

def test_task_func_default_length():
    walk = task_func()
    assert len(walk) == 10001  # Starts at 0, so length is 10000 + 1

def test_task_func_custom_length():
    walk = task_func(length=5000)
    assert len(walk) == 5001  # Starts at 0, so length is 5000 + 1

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_zero_length():
    walk = task_func(length=0)
    assert len(walk) == 1  # Only the starting point

def test_task_func_seed_reproducibility():
    walk1 = task_func(seed=42)
    walk2 = task_func(seed=42)
    assert np.array_equal(walk1, walk2)

def test_task_func_start_at_zero():
    walk = task_func()
    assert walk[0] == 0

def test_task_func_steps_within_range():
    walk = task_func()
    assert all(-1 <= step <= 1 for step in walk)