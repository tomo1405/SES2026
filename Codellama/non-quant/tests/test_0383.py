import matplotlib
from src_0383 import task_func


def test_task_func():
    length = 100
    distribution, ax = task_func(length)
    assert len(distribution) == length
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_legend() == 'Histogram'
    assert ax.get_legend() == 'PDF'