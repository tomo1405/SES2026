import matplotlib
from src_0060 import task_func


def test_task_func_valid_input():
    page_title = "Python (programming language)"
    ax = task_func(page_title)
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_input():
    page_title = "Invalid page title"
    ax = task_func(page_title)
    assert ax is None