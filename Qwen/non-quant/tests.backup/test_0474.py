import pytest
from src_0474 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_negative_walks():
    with pytest.raises(ValueError):
        task_func(-1, 10)

def test_task_func_negative_steps():
    with pytest.raises(ValueError):
        task_func(10, -1)

def test_task_func_zero_walks():
    ax = task_func(0, 10)
    assert len(ax.lines) == 0

def test_task_func_zero_steps():
    ax = task_func(10, 0)
    assert len(ax.lines) == 10
    for line in ax.lines:
        assert len(line.get_xdata()) == 1
        assert len(line.get_ydata()) == 1

def test_task_func_one_walk_one_step():
    ax = task_func(1, 1)
    assert len(ax.lines) == 1
    line = ax.lines[0]
    assert len(line.get_xdata()) == 2
    assert len(line.get_ydata()) == 2
    assert line.get_ydata()[1] in [-1, 1]

def test_task_func_multiple_walks_steps():
    ax = task_func(3, 5, seed=42)
    assert len(ax.lines) == 3
    for i, line in enumerate(ax.lines):
        assert len(line.get_xdata()) == 6
        assert len(line.get_ydata()) == 6
        assert line.get_color() == plt.cm.viridis(i / 3)[:3]

def test_task_func_seed_reproducibility():
    ax1 = task_func(2, 5, seed=42)
    ax2 = task_func(2, 5, seed=42)
    for line1, line2 in zip(ax1.lines, ax2.lines):
        assert np.array_equal(line1.get_ydata(), line2.get_ydata())