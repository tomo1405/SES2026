import matplotlib
import numpy as np
from src_0895 import task_func


def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert array.shape == (ARRAY_SIZE,)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Histogram of Random Integers'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_legend() == ["Mean", "Standard Deviation"]
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_color() == 'red'
    assert ax.get_lines()[0].get_linestyle() == 'dashed'
    assert ax.get_lines()[0].get_linewidth() == 1
    assert ax.get_lines()[1].get_color() == 'purple'
    assert ax.get_lines()[1].get_linestyle() == 'dashed'
    assert ax.get_lines()[1].get_linewidth() == 1
    assert ax.get_lines()[2].get_color() == 'purple'
    assert ax.get_lines()[2].get_linestyle() == 'dashed'
    assert ax.get_lines()[2].get_linewidth() == 1