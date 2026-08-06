python
import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: n=10, seed=0
    fig, points = task_func(10, 0)
    assert len(points) == 10
    assert all(isinstance(p, tuple) and len(p) == 2 for p in points)
    assert all(0 <= p[0] <= 1 and 0 <= p[1] <= 1 for p in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"

    # Test case 2: n=5, seed=1
    fig, points = task_func(5, 1)
    assert len(points) == 5
    assert all(isinstance(p, tuple) and len(p) == 2 for p in points)
    assert all(0 <= p[0] <= 1 and 0 <= p[1] <= 1 for p in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"

    # Test case 3: n=0, seed=0
    with pytest.raises(ValueError):
        task_func(0, 0)

    # Test case 4: n=1000, seed=0
    fig, points = task_func(1000, 0)
    assert len(points) == 1000
    assert all(isinstance(p, tuple) and len(p) == 2 for p in points)
    assert all(0 <= p[0] <= 1 and 0 <= p[1] <= 1 for p in points)
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"