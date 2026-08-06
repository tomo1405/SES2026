import pytest
from src_0129 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_points():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    x, y = fig.axes[0].lines[0].get_data()
    assert len(x) == 100
    assert len(y) == 100

def test_task_func_custom_points():
    fig = task_func(POINTS=50)
    assert isinstance(fig, plt.Figure)
    x, y = fig.axes[0].lines[0].get_data()
    assert len(x) == 50
    assert len(y) == 50

def test_task_func_initial_values():
    fig = task_func()
    x, y = fig.axes[0].lines[0].get_data()
    assert x[0] == 0
    assert y[0] == 0

def test_task_func_random_walk():
    fig = task_func()
    x, y = fig.axes[0].lines[0].get_data()
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        dy = y[i] - y[i - 1]
        assert dx in [-1, 1]
        assert dy in [-1, 1]

def test_task_func_no_show():
    with pytest.raises(AssertionError):
        plt.show = lambda: None
        task_func()