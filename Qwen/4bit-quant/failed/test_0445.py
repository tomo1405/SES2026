import pytest
from src_0445 import task_func
import numpy as np

def test_task_func_default():
    points, ax = task_func()
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_n_points():
    n_points = 50
    points, ax = task_func(n_points=n_points)
    assert isinstance(points, np.ndarray)
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

def test_task_func_invalid_n_points():
    with pytest.raises(ValueError):
        task_func(n_points=-10)

def test_task_func_invalid_n_points_type():
    with pytest.raises(TypeError):
        task_func(n_points="string")

def test_task_func_invalid_random_seed_type():
    with pytest.raises(TypeError):
        task_func(random_seed="string")