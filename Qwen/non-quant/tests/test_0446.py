import numpy as np
import pytest
from src_0446 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError, match="Expected Numpy array"):
        task_func([1, 2, 3])

def test_task_func_min_points():
    with pytest.raises(ValueError, match="Voronoi diagram needs at least 3 points"):
        task_func(np.array([[1, 2]]))

def test_task_func_2d_points():
    with pytest.raises(ValueError, match="Expected array of 2D points"):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]))

def test_task_func_valid_input():
    points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)

def test_task_func_seed_consistency():
    points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
    vor1, _ = task_func(points, seed=42)
    vor2, _ = task_func(points, seed=42)
    assert np.array_equal(vor1.points, vor2.points)
    assert np.array_equal(vor1.ridge_vertices, vor2.ridge_vertices)

def test_task_func_jitter_effect():
    points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
    vor1, _ = task_func(points, seed=42)
    vor2, _ = task_func(points, seed=43)
    assert not np.array_equal(vor1.points, vor2.points)