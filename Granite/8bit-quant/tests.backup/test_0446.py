import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from src_0446 import task_func
import pytest

@pytest.fixture
def points():
    return np.random.rand(10, 2)

def test_input_type(points):
    with pytest.raises(TypeError):
        task_func(points=points.tolist())

def test_input_value(points):
    with pytest.raises(ValueError):
        task_func(points=points[:-1])

def test_output_type(points):
    vor, ax = task_func(points=points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)

def test_seed_effect(points):
    seed1 = 0
    seed2 = 1
    vor1, _ = task_func(points=points, seed=seed1)
    vor2, _ = task_func(points=points, seed=seed2)
    assert not np.array_equal(vor1.points, vor2.points)