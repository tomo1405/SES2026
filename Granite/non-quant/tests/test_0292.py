import pytest
from src_0292 import task_func

def test_task_func():
    # Test case 1: Check if the function returns the expected output for mu=0, sigma=1, and seed=0
    mappable = task_func(mu=0, sigma=1, seed=0)
    assert mappable is not None

    # Test case 2: Check if the function returns the expected output for mu=1, sigma=2, and seed=1
    mappable = task_func(mu=1, sigma=2, seed=1)
    assert mappable is not None

    # Test case 3: Check if the function returns the expected output for mu=-1, sigma=3, and seed=2
    mappable = task_func(mu=-1, sigma=3, seed=2)
    assert mappable is not None