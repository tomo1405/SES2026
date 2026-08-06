import pytest
from src_1059 import task_func
import matplotlib.pyplot as plt

def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 100  # 10 shapes * 10 colors

def test_task_func_custom_pairs():
    ax = task_func(num_pairs=20)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 20

def test_task_func_max_pairs():
    ax = task_func(num_pairs=100)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 100  # 10 shapes * 10 colors

def test_task_func_zero_pairs():
    ax = task_func(num_pairs=0)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0

def test_task_func_negative_pairs():
    ax = task_func(num_pairs=-5)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 0