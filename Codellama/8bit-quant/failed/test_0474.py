import pytest
from src_0474 import task_func

def test_task_func_positive_walks_and_steps():
    n_walks = 10
    n_steps = 10
    seed = 1234
    ax = task_func(n_walks, n_steps, seed)
    assert ax.get_xlim() == (0, n_steps)
    assert ax.get_ylim() == (0, n_walks)
    assert len(ax.get_lines()) == n_walks
    for line in ax.get_lines():
        assert line.get_color() in task_func.COLORS

def test_task_func_negative_walks():
    n_walks = -1
    n_steps = 10
    seed = 1234
    with pytest.raises(ValueError):
        task_func(n_walks, n_steps, seed)

def test_task_func_negative_steps():
    n_walks = 10
    n_steps = -1
    seed = 1234
    with pytest.raises(ValueError):
        task_func(n_walks, n_steps, seed)