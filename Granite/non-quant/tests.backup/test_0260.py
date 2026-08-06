import matplotlib
import numpy as np
import pytest
from src_0260 import task_func

@pytest.fixture
def ax():
    return matplotlib.pyplot.axes()

def test_task_func_with_valid_input(ax):
    num_points = 100
    result = task_func(ax, num_points)
    assert isinstance(result, matplotlib.axes.Axes)

def test_task_func_with_invalid_input(ax):
    num_points = "invalid"
    with pytest.raises(ValueError):
        task_func(ax, num_points)

def test_task_func_with_invalid_ax_type():
    ax = "invalid"
    num_points = 100
    with pytest.raises(ValueError):
        task_func(ax, num_points)