import pytest
from src_0909 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pattern = '*.csv'
    plots = task_func(directory, pattern)
    assert len(plots) > 0
    for plot in plots:
        assert isinstance(plot, matplotlib.axes.Axes)
        assert plot.get_title() == 'Monthly Sales'
        assert plot.get_xlabel() == 'Month'
        assert plot.get_ylabel() == 'Sales'