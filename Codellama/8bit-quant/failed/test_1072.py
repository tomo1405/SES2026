import pytest
from src_1072 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fig, ax = task_func(list_of_lists)
    assert len(fig.axes) == len(list_of_lists)
    assert len(ax.lines) == len(list_of_lists)
    assert all(ax.lines[i].get_color() == COLORS[i % len(COLORS)] for i in range(len(list_of_lists)))