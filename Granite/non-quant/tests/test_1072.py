import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
COLORS = ["b", "g", "r", "c", "m", "y", "k"]
def task_func(list_of_lists):
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)

    for list_ in list_of_lists:
        y_values = np.arange(1, len(list_) + 1)
        shuffle(y_values)
        ax.plot(y_values, next(color_cycle))

    return fig, ax

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fig, ax = task_func(list_of_lists)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.get_lines()) == len(list_of_lists)
    for line in ax.get_lines():
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        assert len(xdata) == len(ydata)
        assert all(x > 0 and x <= len(list_) for x in xdata)
        assert all(y > 0 and y <= len(list_) for y in ydata)