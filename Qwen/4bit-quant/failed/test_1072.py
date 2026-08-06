import pytest
from src_1072 import task_func
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

def test_task_func_with_empty_list():
    fig, ax = task_func([])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert not ax.lines  # No lines should be plotted

def test_task_func_with_single_list():
    fig, ax = task_func([[1, 2, 3]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1  # One line should be plotted

def test_task_func_with_multiple_lists():
    fig, ax = task_func([[1, 2], [3, 4, 5], [6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # Three lines should be plotted

def test_task_func_with_different_lengths():
    fig, ax = task_func([[1], [2, 3], [4, 5, 6]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 3  # Three lines should be plotted

def test_task_func_with_color_cycle():
    fig, ax = task_func([[1, 2], [3, 4], [5, 6, 7], [8, 9, 10, 11]])
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 4  # Four lines should be plotted
    colors = [line.get_color() for line in ax.lines]
    assert colors == ["b", "g", "r", "c"]  # Colors should cycle through the list

def test_task_func_with_shuffled_y_values():
    fig, ax = task_func([[1, 2, 3]])
    line = ax.lines[0]
    y_values = line.get_ydata()
    assert len(y_values) == 3
    assert set(y_values) == {1, 2, 3}  # Y values should be a permutation of [1, 2, 3]

def test_task_func_with_no_shuffle():
    fig, ax = task_func([[1, 2, 3]], shuffle=False)
    line = ax.lines[0]
    y_values = line.get_ydata()
    assert list(y_values) == [1, 2, 3]  # Y values should be in the original order