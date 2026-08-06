import pytest
from src_0260 import task_func
import matplotlib.axes
import numpy as np

def test_task_func_valid_input():
    ax = matplotlib.axes.Axes()
    num_points = 10
    result = task_func(ax, num_points)
    assert isinstance(result, matplotlib.axes.Axes)
    assert len(result.lines) == 1
    assert result.lines[0].get_xdata() == theta
    assert result.lines[0].get_ydata() == r
    assert result.get_rlabel_position() == num_points / 10

def test_task_func_invalid_input():
    ax = "not an axes"
    num_points = 10
    with pytest.raises(ValueError):
        task_func(ax, num_points)