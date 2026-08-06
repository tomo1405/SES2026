import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import pytest

def test_task_func_type_error():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(TypeError):
        task_func(points, seed=0)

def test_task_func_value_error():
    points = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        task_func(points, seed=0)

def test_task_func_shape_error():
    points = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        task_func(points, seed=0)

def test_task_func_success():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    vor, ax = task_func(points, seed=0)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)
    assert vor.points.shape == (3, 2)
    assert vor.regions.shape == (3, 2)
    assert vor.vertices.shape == (3, 2)
    assert vor.ridge_points.shape == (3, 2)
    assert vor.ridge_vertices.shape == (3, 2)
    assert vor.point_region.shape == (3,)
    assert vor.point_region.dtype == np.int64
    assert vor.regions.dtype == np.int64
    assert vor.vertices.dtype == np.int64
    assert vor.ridge_points.dtype == np.int64
    assert vor.ridge_vertices.dtype == np.int64
    assert vor.point_region.min() >= 0
    assert vor.point_region.max() < 3
    assert vor.regions.min() >= 0
    assert vor.regions.max() < 3
    assert vor.vertices.min() >= 0
    assert vor.vertices.max() < 3
    assert vor.ridge_points.min() >= 0
    assert vor.ridge_points.max() < 3
    assert vor.ridge_vertices.min() >= 0
    assert vor.ridge_vertices.max() < 3
    assert ax.get_xlim() == (1, 5)
    assert ax.get_ylim() == (2, 6)