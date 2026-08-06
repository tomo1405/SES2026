import numpy as np
import random
import pytest

from src_0900 import task_func

def test_task_func_length_negative():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_seed_not_ affecting_output():
    walk1 = task_func(length=100, seed=0)
    walk2 = task_func(length=100, seed=0)
    walk3 = task_func(length=100, seed=1)
    assert np.array_equal(walk1, walk2)
    assert not np.array_equal(walk1, walk3)

def test_task_func_output_type():
    walk = task_func(length=100)
    assert isinstance(walk, np.ndarray)

def test_task_func_output_values():
    walk = task_func(length=100)
    assert np.all(walk >= 0)  # Check that all elements are non-negative
    assert np.all(np.diff(walk) == 1)  # Check that the walk is always increasing by 1