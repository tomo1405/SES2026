python
import pytest
import matplotlib
import numpy as np

from src_0260 import task_func

def test_task_func():
    fig, ax = plt.subplots()
    num_points = 100
    ax = task_func(ax, num_points)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'theta'
    assert ax.get_ylabel() == 'r'
    assert len(ax.collections) == 1
    assert len(ax.collections[0].get_offsets()) == num_points