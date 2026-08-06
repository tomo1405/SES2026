import pytest
from src_1072 import task_func
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

def test_task_func():
    # Test with empty input
    fig, ax = task_func([])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0

    # Test with one empty list
    fig, ax = task_func([[]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 0

    # Test with one non-empty list
    fig, ax = task_func([[1, 2, 3]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 3
    assert len(ax.lines[0].get_ydata()) == 3

    # Test with multiple lists
    fig, ax = task_func([[1, 2], [3, 4, 5], [6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3
    assert len(ax.lines[0].get_xdata()) == 2
    assert len(ax.lines[0].get_ydata()) == 2
    assert len(ax.lines[1].get_xdata()) == 3
    assert len(ax.lines[1].get_ydata()) == 3
    assert len(ax.lines[2].get_xdata()) == 1
    assert len(ax.lines[2].get_ydata()) == 1

    # Test with different lengths of lists
    fig, ax = task_func([[1], [2, 3], [4, 5, 6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3
    assert len(ax.lines[0].get_xdata()) == 1
    assert len(ax.lines[0].get_ydata()) == 1
    assert len(ax.lines[1].get_xdata()) == 2
    assert len(ax.lines[1].get_ydata()) == 2
    assert len(ax.lines[2].get_xdata()) == 3
    assert len(ax.lines[2].get_ydata()) == 3

    # Test with colors cycling
    fig, ax = task_func([[1, 2], [3, 4, 5], [6]])
    colors = set(line.get_color() for line in ax.lines)
    assert colors == {"b", "g", "r"}

    # Test with shuffled y-values
    fig, ax = task_func([[1, 2, 3]])
    y_data = ax.lines[0].get_ydata()
    assert sorted(y_data) == [1, 2, 3]
    assert y_data != [1, 2, 3]  # Ensure y-values are shuffled