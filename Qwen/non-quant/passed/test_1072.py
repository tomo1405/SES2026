import pytest
from src_1072 import task_func
import matplotlib.pyplot as plt
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
    line = ax.lines[0]
    assert len(line.get_xdata()) == 3
    assert len(line.get_ydata()) == 3

    # Test with multiple lists
    fig, ax = task_func([[1, 2], [3, 4, 5], [6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3
    for i, line in enumerate(ax.lines):
        assert len(line.get_xdata()) == len(list_of_lists[i])
        assert len(line.get_ydata()) == len(list_of_lists[i])

    # Test with different lengths of lists
    fig, ax = task_func([[1], [2, 3], [4, 5, 6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3
    for i, line in enumerate(ax.lines):
        assert len(line.get_xdata()) == len(list_of_lists[i])
        assert len(line.get_ydata()) == len(list_of_lists[i])

    # Test with shuffled y-values
    list_of_lists = [[1, 2, 3], [4, 5], [6]]
    fig, ax = task_func(list_of_lists)
    for i, line in enumerate(ax.lines):
        assert set(line.get_ydata()) == set(np.arange(1, len(list_of_lists[i]) + 1))

    # Test with more lists than colors
    list_of_lists = [[1], [2], [3], [4], [5], [6], [7], [8]]
    fig, ax = task_func(list_of_lists)
    assert len(ax.lines) == len(list_of_lists)
    for i, line in enumerate(ax.lines):
        assert line.get_color() == COLORS[i % len(COLORS)]

    # Test with no shuffling
    list_of_lists = [[1, 2, 3], [4, 5], [6]]
    original_y_values = [np.arange(1, len(lst) + 1) for lst in list_of_lists]
    fig, ax = task_func(list_of_lists)
    for i, line in enumerate(ax.lines):
        assert np.array_equal(line.get_ydata(), original_y_values[i])

    plt.close(fig)