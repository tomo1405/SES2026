import pytest
from src_0260 import task_func
import matplotlib.axes
import numpy as np

def test_task_func():
    ax = matplotlib.axes.Axes()
    num_points = 10
    result = task_func(ax, num_points)
    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_rlabel_position() == num_points / 10
    assert len(result.get_lines()) == 1
    assert result.get_lines()[0].get_xdata() == theta
    assert result.get_lines()[0].get_ydata() == r