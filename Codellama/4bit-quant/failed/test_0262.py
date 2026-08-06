import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    ax = plt.PolarAxes()
    radius = 10
    ax = task_func(ax, radius)
    assert ax.get_rlabel_position() == radius * 45
    assert len(ax.lines) == 1
    assert ax.lines[0].get_xdata() == np.linspace(0, 2 * np.pi, 1000)
    assert ax.lines[0].get_ydata() == np.ones_like(np.linspace(0, 2 * np.pi, 1000))

def test_task_func_invalid_radius():
    ax = plt.PolarAxes()
    radius = -1
    with pytest.raises(ValueError):
        task_func(ax, radius)

def test_task_func_invalid_ax():
    ax = plt.Axes()
    radius = 10
    with pytest.raises(TypeError):
        task_func(ax, radius)