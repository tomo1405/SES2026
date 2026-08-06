import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from src_0446 import task_func
import pytest

def test_task_func_with_valid_input():
    points = np.array([[0, 0], [1, 1], [2, 2]])
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func("invalid input")
    with pytest.raises(ValueError):
        task_func(np.array([[0, 0]]))
    with pytest.raises(ValueError):
        task_func(np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]))
    with pytest.raises(ValueError):
        task_func(np.array([[0, 0, 0], [1, 1, 1]]))