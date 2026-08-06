import pytest
from src_0474 import task_func

def test_task_func():
    n_walks = 10
    n_steps = 10
    seed = 1234
    ax = task_func(n_walks, n_steps, seed)
    assert ax.get_xlabel() == "Step"
    assert ax.get_ylabel() == "Walk"
    assert ax.get_title() == "Random Walk"
    assert len(ax.get_lines()) == n_walks
    for line in ax.get_lines():
        assert line.get_color() in ["b", "g", "r", "c", "m", "y", "k"]