import pytest
from src_0319 import task_func
import matplotlib.pyplot as plt

def test_task_func_output():
    ax = task_func(points_count=10, radius=1)
    assert isinstance(ax, plt.Axes)

def test_task_func_point_count():
    ax = task_func(points_count=10, radius=1)
    lines, = ax.get_lines()
    assert len(lines.get_xdata()) == 10

def test_task_func_radius():
    ax = task_func(points_count=10, radius=2)
    lines, = ax.get_lines()
    distances = [math.sqrt(x**2 + y**2) for x, y in zip(lines.get_xdata(), lines.get_ydata())]
    assert all(distance <= 2 for distance in distances)

def test_task_func_default_parameters():
    ax = task_func()
    lines, = ax.get_lines()
    assert len(lines.get_xdata()) == 1000

def test_task_func_aspect_ratio():
    ax = task_func(points_count=10, radius=1)
    assert ax.get_aspect() == 'equal'