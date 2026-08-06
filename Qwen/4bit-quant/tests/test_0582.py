import matplotlib.pyplot as plt
import numpy as np
from src_0582 import task_func


def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == SIZE
    assert len(ax.lines[0].get_ydata()) == SIZE

def test_task_func_custom_size():
    custom_size = 500
    ax = task_func(size=custom_size)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == custom_size
    assert len(ax.lines[0].get_ydata()) == custom_size

def test_task_func_custom_frequency():
    custom_frequency = 3
    ax = task_func(frequency=custom_frequency)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == SIZE
    assert len(ax.lines[0].get_ydata()) == SIZE

def test_task_func_randomness():
    ax1 = task_func()
    ax2 = task_func()
    assert isinstance(ax1, plt.Axes)
    assert isinstance(ax2, plt.Axes)
    assert not np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata())

def test_task_func_plot_content():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == ''
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''
    assert len(ax.get_lines()) == 1