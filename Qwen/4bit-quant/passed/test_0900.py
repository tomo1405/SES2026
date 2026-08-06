import pytest
from src_0900 import task_func
import numpy as np

def test_task_func_length_zero():
    result = task_func(length=0)
    assert len(result) == 1, "The walk should start with 0, so the length should be 1"
    assert result[0] == 0, "The first element should be 0"

def test_task_func_length_positive():
    result = task_func(length=10)
    assert len(result) == 11, "The walk should have one more element than the length parameter"
    assert result[0] == 0, "The first element should be 0"

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_seed_consistency():
    walk1 = task_func(length=10, seed=42)
    walk2 = task_func(length=10, seed=42)
    assert np.array_equal(walk1, walk2), "The walks should be identical for the same seed"

def test_task_func_randomness():
    walk1 = task_func(length=10, seed=0)
    walk2 = task_func(length=10, seed=1)
    assert not np.array_equal(walk1, walk2), "The walks should differ for different seeds"

def test_task_func_start_at_zero():
    result = task_func(length=10)
    assert result[0] == 0, "The walk should start at 0"

def test_task_func_correct_steps():
    result = task_func(length=10, seed=0)
    steps = np.diff(result)
    assert all(step in [-1, 1] for step in steps), "All steps should be either 1 or -1"