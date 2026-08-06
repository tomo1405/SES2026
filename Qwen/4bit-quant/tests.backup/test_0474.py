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

def test_task_func_one_walk():
    ax = task_func(1, 5)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 5

def test_task_func_multiple_walks():
    ax = task_func(3, 5)
    assert len(ax.lines) == 3
    for line in ax.lines:
        assert len(line.get_xdata()) == 5

def test_task_func_with_seed():
    ax1 = task_func(1, 5, seed=42)
    ax2 = task_func(1, 5, seed=42)
    assert np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())

def test_task_func_color_cycle():
    ax = task_func(7, 5)
    colors = ["b", "g", "r", "c", "m", "y", "k"]
    for i, line in enumerate(ax.lines):
        assert line.get_color() == colors[i % len(colors)]

def test_task_func_plot_type():
    ax = task_func(1, 5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1