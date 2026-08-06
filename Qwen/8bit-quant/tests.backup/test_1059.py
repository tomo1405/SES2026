import pytest
from src_1059 import task_func
import matplotlib.pyplot as plt

def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 10  # Default number of pairs is 10

def test_task_func_max_pairs():
    ax = task_func(num_pairs=100)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == len(SHAPES) * len(COLORS)  # Maximum number of pairs

def test_task_func_zero_pairs():
    ax = task_func(num_pairs=0)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0  # No pairs should be plotted

def test_task_func_negative_pairs():
    ax = task_func(num_pairs=-5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0  # Negative number of pairs should result in no plotting

def test_task_func_specific_number_of_pairs():
    num_pairs = 5
    ax = task_func(num_pairs=num_pairs)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == num_pairs  # Specific number of pairs should be plotted