import matplotlib
import numpy as np
import pytest

from src_0260 import task_func

@pytest.mark.parametrize("ax, num_points", [
    (matplotlib.pyplot.axes(), 10),
    (matplotlib.pyplot.axes(), 20),
    (matplotlib.pyplot.axes(), 30),
])
def test_task_func(ax, num_points):
    with pytest.raises(ValueError):
        task_func(ax, num_points)

    ax = task_func(ax, num_points)
    assert isinstance(ax, matplotlib.axes.Axes)