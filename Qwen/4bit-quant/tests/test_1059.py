import pytest
from src_1059 import task_func
import matplotlib.pyplot as plt

def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 100  # 10 shapes * 10 colors

def test_task_func_custom_pairs():
    ax = task_func(num_pairs=50)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 50

def test_task_func_zero_pairs():
    ax = task_func(num_pairs=0)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0

def test_task_func_more_than_max_pairs():
    ax = task_func(num_pairs=1000)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 100  # Max pairs is 100

def test_task_func_negative_pairs():
    ax = task_func(num_pairs=-10)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0  # Negative pairs should result in no pairs