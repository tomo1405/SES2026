python
import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: n=10, seed=0
    n = 10
    seed = 0
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"
    assert all(isinstance(x, float) and isinstance(y, float) for x, y in points)

    # Test case 2: n=5, seed=1
    n = 5
    seed = 1
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert fig.axes[0].get_title() == "Scatter plot of random points"
    assert fig.axes[0].get_xlabel() == "X"
    assert fig.axes[0].get_ylabel() == "Y"
    assert all(isinstance(x, float) and isinstance(y, float) for x, y in points)

    # Test case 3: n=0, seed=0 (should raise ValueError)
    n = 0
    seed = 0
    with pytest.raises(ValueError):
        task_func(n, seed)

    # Test case 4: n=10, seed=None (should raise TypeError)
    n = 10
    seed = None
    with pytest.raises(TypeError):
        task_func(n, seed)