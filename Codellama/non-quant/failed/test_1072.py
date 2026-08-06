import pytest
from src_1072 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fig, ax = task_func(list_of_lists)
    assert len(ax.lines) == 3
    assert all(line.get_color() in COLORS for line in ax.lines)
    assert all(line.get_ydata() == np.arange(1, len(list_) + 1) for list_ in list_of_lists)
    assert all(line.get_xdata() == np.arange(1, len(list_) + 1) for list_ in list_of_lists)