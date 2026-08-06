import numpy as np
import random
import pytest
from src_0900 import task_func

def test_task_func_valid_input():
    assert task_func(length=10000, seed=0).shape == (10001,)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(length=-1, seed=0)

def test_task_func_seed():
    walk1 = task_func(length=10000, seed=0)
    walk2 = task_func(length=10000, seed=0)
    assert np.array_equal(walk1, walk2)

def test_task_func_seed_different():
    walk1 = task_func(length=10000, seed=0)
    walk2 = task_func(length=10000, seed=1)
    assert not np.array_equal(walk1, walk2)