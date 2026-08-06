import pytest
from src_0474 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_negative_input():
    with pytest.raises(ValueError):
        task_func(-1, 10)
    with pytest.raises(ValueError):
        task_func(10, -1)

def test_task_func_zero_input():
    ax = task_func(0, 10)
    assert len(ax.lines) == 0

def test_task_func_single_walk():
    ax = task_func(1, 10, seed=42)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 11
    assert len(ax.lines[0].get_ydata()) == 11

def test_task_func_multiple_walks():
    ax = task_func(3, 10, seed=42)
    assert len(ax.lines) == 3
    for line in ax.lines:
        assert len(line.get_xdata()) == 11
        assert len(line.get_ydata()) == 11

def test_task_func_colors():
    ax = task_func(7, 10, seed=42)
    colors = ["b", "g", "r", "c", "m", "y", "k"]
    for i, line in enumerate(ax.lines):
        assert line.get_color() == colors[i]

def test_task_func_no_seed():
    ax1 = task_func(1, 10)
    ax2 = task_func(1, 10)
    assert not np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())

def test_task_func_with_seed():
    ax1 = task_func(1, 10, seed=42)
    ax2 = task_func(1, 10, seed=42)
    assert np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())