import pytest
from src_0445 import task_func
import numpy as np

def test_task_func_default():
    points, ax = task_func()
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_n_points():
    n_points = 50
    points, ax = task_func(n_points=n_points)
    assert points.shape == (n_points, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    random_seed = 42
    points1, _ = task_func(random_seed=random_seed)
    points2, _ = task_func(random_seed=random_seed)
    assert np.array_equal(points1, points2)

def test_task_func_no_random_seed():
    points1, _ = task_func(random_seed=None)
    points2, _ = task_func(random_seed=None)
    assert not np.array_equal(points1, points2)

def test_task_func_plot():
    points, ax = task_func()
    assert len(ax.collections) == 1  # One scatter plot collection
    assert ax.collections[0].get_offsets().shape == (100, 3)