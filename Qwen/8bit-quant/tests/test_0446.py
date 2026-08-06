import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0446 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_input_length():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2]]))

def test_task_func_input_shape():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4, 5]]))

def test_task_func_output_type():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)

def test_task_func_jitter():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    vor, _ = task_func(points, seed=0)
    jittered_points = points + np.random.normal(0, 1e-10, points.shape)
    np.testing.assert_array_almost_equal(vor.points, jittered_points, decimal=10)

def test_task_func_figure_creation():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    _, ax = task_func(points)
    assert ax is not None