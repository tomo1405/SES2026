import pytest
from src_0213 import task_func
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6)]
    ax, max_y_point = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    assert ax.get_legend() == 'Points'
    assert ax.get_legend() == 'Max Y Point'
    assert max_y_point == (5, 6)
    assert np.array_equal(ax.get_xdata(), np.array([1, 3, 5]))
    assert np.array_equal(ax.get_ydata(), np.array([2, 4, 6]))