import pytest
from src_0909 import task_func

def test_task_func():
    directory = 'path/to/directory'
    pattern = 'pattern'
    plots = task_func(directory, pattern)
    assert len(plots) > 0
    for plot in plots:
        assert isinstance(plot, matplotlib.axes.Axes)