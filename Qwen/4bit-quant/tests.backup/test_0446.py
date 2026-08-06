import pytest
from src_0446 import task_func
import numpy as np

def test_task_func_type_error():
    with pytest.raises(TypeError, match="Expected Numpy array"):
        task_func([1, 2, 3])

def test_task_func_value_error_too_few_points():
    with pytest.raises(ValueError, match="Voronoi diagram needs at least 3 points"):
        task_func(np.array([[1, 2]]))

def test_task_func_value_error_not_2d_points():
    with pytest.raises(ValueError, match="Expected array of 2D points"):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]))

def test_task_func_valid_input():
    points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
    vor1, _ = task_func(points, seed=0)
    vor2, _ = task_func(points, seed=0)
    assert np.array_equal(vor1.points, vor2.points)
    assert np.array_equal(vor1.regions, vor2.regions)
    assert np.array_equal(vor1.ridge_vertices, vor2.ridge_vertices)
    assert np.array_equal(vor1.ridge_points, vor2.ridge_points)
    assert np.array_equal(vor1.point_region, vor2.point_region)