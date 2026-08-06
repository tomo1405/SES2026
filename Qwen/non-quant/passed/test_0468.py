import pytest
from src_0468 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_output():
    n = 5
    seed = 42
    fig, points = task_func(n, seed)
    
    # Check if the number of points is correct
    assert len(points) == n
    
    # Check if the points are within the expected range [0, 1)
    for x, y in points:
        assert 0 <= x < 1
        assert 0 <= y < 1
    
    # Check if the figure is a matplotlib Figure object
    assert isinstance(fig, plt.Figure)
    
    # Check if the axes have the correct title and labels
    ax = fig.axes[0]
    assert ax.get_title() == "Scatter plot of random points"
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"

def test_task_func_reproducibility():
    n = 5
    seed = 42
    _, points1 = task_func(n, seed)
    _, points2 = task_func(n, seed)
    
    # Check if the same seed produces the same points
    assert points1 == points2