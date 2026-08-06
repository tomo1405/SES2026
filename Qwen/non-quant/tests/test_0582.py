import matplotlib.pyplot as plt
import numpy as np
from src_0582 import task_func


def test_task_func_default():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    x_data, y_data = ax.lines[0].get_data()
    assert len(x_data) == SIZE
    assert len(y_data) == SIZE

def test_task_func_custom_size():
    custom_size = 500
    ax = task_func(size=custom_size)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    x_data, y_data = ax.lines[0].get_data()
    assert len(x_data) == custom_size
    assert len(y_data) == custom_size

def test_task_func_custom_frequency():
    custom_frequency = 2
    ax = task_func(frequency=custom_frequency)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    x_data, y_data = ax.lines[0].get_data()
    assert len(x_data) == SIZE
    assert len(y_data) == SIZE

def test_task_func_randomness():
    ax1 = task_func()
    ax2 = task_func()
    x_data1, y_data1 = ax1.lines[0].get_data()
    x_data2, y_data2 = ax2.lines[0].get_data()
    assert not np.array_equal(y_data1, y_data2)