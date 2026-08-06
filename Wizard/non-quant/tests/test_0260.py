python
import matplotlib
import numpy as np
import pytest

def task_func(ax, num_points):
    
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("The input is not an axes")

    r = np.random.rand(num_points)
    theta = 2 * np.pi * np.random.rand(num_points)

    ax.scatter(theta, r)
    ax.set_rlabel_position(num_points / 10)
    return ax

def test_task_func():
    fig, ax = plt.subplots()
    task_func(ax, 10)
    assert ax.get_xlabel() == 'theta'
    assert ax.get_ylabel() == 'r'
    assert ax.get_rlabel_position() == 0.5