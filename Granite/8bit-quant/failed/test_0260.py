import matplotlib
import numpy as np
import pytest
from src_0260 import task_func

@pytest.mark.parametrize("ax, num_points", [
    (matplotlib.pyplot.axes(), 10),
    (matplotlib.pyplot.axes(), 20),
    (matplotlib.pyplot.axes(), 30),
])
def test_task_func_valid_input(ax, num_points):
    assert isinstance(task_func(ax, num_points), matplotlib.axes.Axes)

@pytest.mark.parametrize("ax, num_points", [
    (None, 10),
    (10, 10),
    ("axes", 10),
])
def test_task_func_invalid_input(ax, num_points):
    with pytest.raises(ValueError):
        task_func(ax, num_points)