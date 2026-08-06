import pytest
from src_0446 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def test_task_func():
    # Test case 1: Basic functionality
    points = np.array([[0, 0], [1, 0], [0, 1]])
    vor, ax = task_func(points)
    assert isinstance(vor, Voronoi), "Expected Voronoi object"
    assert isinstance(ax, plt.Axes), "Expected matplotlib Axes object"

    # Add more test cases as needed

    # Add more test cases to cover different scenarios