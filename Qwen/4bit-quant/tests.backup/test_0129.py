import pytest
from src_0129 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_points():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1

def test_task_func_custom_points():
    fig = task_func(50)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1

def test_task_func_array_lengths():
    fig = task_func(100)
    ax = fig.axes[0]
    line, = ax.get_lines()
    xdata, ydata = line.get_data()
    assert len(xdata) == 100
    assert len(ydata) == 100

def test_task_func_plot_values():
    fig = task_func(3)
    ax = fig.axes[0]
    line, = ax.get_lines()
    xdata, ydata = line.get_data()
    np.testing.assert_almost_equal(xdata, [0., 0., -1.], decimal=6)
    np.testing.assert_almost_equal(ydata, [0., 0., 0.], decimal=6)

def test_task_func_randomness():
    fig1 = task_func(10)
    fig2 = task_func(10)
    ax1 = fig1.axes[0]
    ax2 = fig2.axes[0]
    line1, = ax1.get_lines()
    line2, = ax2.get_lines()
    xdata1, ydata1 = line1.get_data()
    xdata2, ydata2 = line2.get_data()
    assert not np.array_equal(xdata1, xdata2)
    assert not np.array_equal(ydata1, ydata2)