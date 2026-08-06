import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: Default arguments
    fig, points = task_func(100)
    assert fig is not None
    assert points is not None
    assert len(points) == 100

    # Test case 2: Custom arguments
    fig, points = task_func(50, seed=42)
    assert fig is not None
    assert points is not None
    assert len(points) == 50