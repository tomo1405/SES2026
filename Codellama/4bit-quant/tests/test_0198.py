import pytest
from src_0198 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8, 10]
    N = 3

    ax = task_func(l1, l2, N)

    assert len(ax.lines) == N
    assert ax.lines[0].get_xdata() == [0, 1, 2, 3, 4]
    assert ax.lines[0].get_ydata() == [1, 2, 3, 4, 5]
    assert ax.lines[1].get_xdata() == [0, 1, 2, 3, 4]
    assert ax.lines[1].get_ydata() == [2, 4, 6, 8, 10]
    assert ax.lines[2].get_xdata() == [0, 1, 2, 3, 4]
    assert ax.lines[2].get_ydata() == [3, 6, 9, 12, 15]