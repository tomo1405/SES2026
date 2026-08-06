import pytest
from src_0445 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    points, ax = task_func(n_points=100, random_seed=42)
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.name == "3d"