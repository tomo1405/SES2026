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
    walk = task_func(length=10, seed=0)
    assert len(walk) == 11
    assert walk[0] == 0
    assert walk[1] == 1
    assert walk[2] == 1
    assert walk[3] == 2
    assert walk[4] == 1
    assert walk[5] == -1
    assert walk[6] == -1
    assert walk[7] == -2
    assert walk[8] == -1
    assert walk[9] == 1
    assert walk[10] == 0
    
    # Test case 2: length=100, seed=1
    walk = task_func(length=100, seed=1)
    assert len(walk) == 101
    assert walk[0] == 0
    assert walk[1] == 1
    assert walk[2] == 1
    assert walk[3] == 2
    assert walk[4] == 1
    assert walk[5] == -1
    assert walk[6] == -1
    assert walk[7] == -2
    assert walk[8] == -1
    assert walk[9] == 1
    assert walk[10] == 0
    assert walk[100] == 0
    
    # Test case 3: length=0, seed=0
    walk = task_func(length=0, seed=0)
    assert len(walk) == 1
    
    # Test case 4: length=-1, seed=0
    with pytest.raises(ValueError):
        walk = task_func(length=-1, seed=0)