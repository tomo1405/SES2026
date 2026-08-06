import matplotlib
import numpy as np
from src_0445 import task_func


def test_task_func():
    points, ax = task_func()
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_zlabel() == "Z"
    assert ax.get_title() == "3D Scatter Plot"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_zlim() == (0, 1)