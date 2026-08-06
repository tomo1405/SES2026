import pytest
from src_0319 import task_func

def test_task_func_default():
    ax = task_func()
    assert ax.get_title() == ''
    assert len(ax.collections) == 1  # There should be one collection of points

def test_task_func_custom_points_count():
    ax = task_func(points_count=500)
    assert len(ax.collections[0].get_offsets()) == 500

def test_task_func_custom_radius():
    ax = task_func(radius=2)
    points = ax.collections[0].get_offsets()
    for x, y in points:
        assert math.sqrt(x**2 + y**2) <= 2

def test_task_func_aspect_ratio():
    ax = task_func()
    assert ax.get_aspect() == 'equal'

def test_task_func_plot_type():
    ax = task_func()
    assert isinstance(ax, plt.Axes)