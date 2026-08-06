import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: Test with n=10 and seed=0
    fig, points = task_func(n=10, seed=0)
    assert fig is not None
    assert len(points) == 10

    # Test case 2: Test with n=5 and seed=1
    fig, points = task_func(n=5, seed=1)
    assert fig is not None
    assert len(points) == 5

    # Test case 3: Test with n=1 and seed=2
    fig, points = task_func(n=1, seed=2)
    assert fig is not None
    assert len(points) == 1