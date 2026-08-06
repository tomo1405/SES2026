import matplotlib
from src_0101 import task_func


def test_task_func():
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Random Time Series Data'
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == 'Value over Time'