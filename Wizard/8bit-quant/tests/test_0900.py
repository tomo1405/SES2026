python
import numpy as np
import random
import pytest

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("length must be a non-negative integer")
    random.seed(seed)
    steps = [1 if random.random() > 0.5 else -1 for _ in range(length)]
    walk = np.cumsum([0] + steps)  # Starts at 0
    return walk

def test_task_func():
    # Test case 1: length=10, seed=0
    assert len(task_func(10, 0)) == 11
    # Test case 2: length=100, seed=1
    assert len(task_func(100, 1)) == 101
    # Test case 3: length=0, seed=2
    with pytest.raises(ValueError):
        task_func(0, 2)
    # Test case 4: length=-1, seed=3
    with pytest.raises(ValueError):
        task_func(-1, 3)