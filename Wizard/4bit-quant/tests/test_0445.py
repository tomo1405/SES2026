python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(n_points=100, random_seed=None):
    np.random.seed(random_seed)
    points = np.random.random((n_points, 3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])

    return points, ax

def test_task_func():
    points, ax = task_func()
    assert points.shape == (100, 3)
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_zlabel() == 'Z'
    assert ax.get_title() == '3D Scatter Plot'