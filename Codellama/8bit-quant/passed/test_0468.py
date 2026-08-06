import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: n = 10, seed = 0
    n = 10
    seed = 0
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(0 <= x <= 1 for x, _ in points)
    assert all(0 <= y <= 1 for _, y in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"

    # Test case 2: n = 10, seed = 1
    n = 10
    seed = 1
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(0 <= x <= 1 for x, _ in points)
    assert all(0 <= y <= 1 for _, y in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"

    # Test case 3: n = 10, seed = 2
    n = 10
    seed = 2
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(0 <= x <= 1 for x, _ in points)
    assert all(0 <= y <= 1 for _, y in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"