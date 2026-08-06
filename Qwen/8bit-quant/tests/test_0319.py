import pytest
from src_0319 import task_func
import matplotlib.pyplot as plt

def test_task_func_default_values():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # There should be one scatter plot collection
    assert len(ax.collections[0].get_offsets()) == 1000  # Default points_count is 1000

def test_task_func_custom_values():
    points_count = 500
    radius = 2
    ax = task_func(points_count, radius)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # There should be one scatter plot collection
    assert len(ax.collections[0].get_offsets()) == points_count  # Custom points_count is 500

def test_task_func_zero_points():
    ax = task_func(points_count=0)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 0  # No scatter plot collection if points_count is 0

def test_task_func_negative_radius():
    with pytest.raises(ValueError):
        task_func(radius=-1)

def test_task_func_non_integer_points_count():
    with pytest.raises(TypeError):
        task_func(points_count=1000.5)

def test_task_func_non_positive_points_count():
    with pytest.raises(ValueError):
        task_func(points_count=-1000)