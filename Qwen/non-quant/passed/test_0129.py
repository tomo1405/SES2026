import pytest
from src_0129 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_points():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    x_data, y_data = ax.get_lines()[0].get_data()
    assert len(x_data) == 100
    assert len(y_data) == 100

def test_task_func_custom_points():
    fig = task_func(50)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    x_data, y_data = ax.get_lines()[0].get_data()
    assert len(x_data) == 50
    assert len(y_data) == 50

def test_task_func_initial_values():
    fig = task_func()
    ax = fig.axes[0]
    x_data, y_data = ax.get_lines()[0].get_data()
    assert x_data[0] == 0
    assert y_data[0] == 0

def test_task_func_plot_lines():
    fig = task_func()
    ax = fig.axes[0]
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_linestyle() == '-'