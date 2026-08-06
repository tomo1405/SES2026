from src_0406 import task_func


def test_task_func():
    points = 10
    y, ax = task_func(points)
    assert len(y) == points
    assert len(ax.lines) == 1
    assert ax.lines[0].get_xdata() == x
    assert ax.lines[0].get_ydata() == y