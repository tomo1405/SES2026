import numpy as np
from src_0556 import task_func


def test_task_func():
    a = np.random.rand(100)
    b = np.random.rand(100)
    correlation, _ = task_func(a, b)
    assert isinstance(correlation, float)
    assert 0 <= correlation <= 1

def test_task_func_plot():
    a = np.random.rand(100)
    b = np.random.rand(100)
    _, ax = task_func(a, b)
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata = lines[0].get_xdata()
    ydata = lines[0].get_ydata()
    assert len(xdata) == len(ydata)
    assert np.all(xdata == np.unique(a))