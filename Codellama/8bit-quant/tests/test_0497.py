import matplotlib
import pytest
from src_0497 import task_func


def test_task_func_days_in_past_less_than_1():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

def test_task_func_days_in_past_greater_than_1():
    ax = task_func(days_in_past=7)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature (°C)"
    assert ax.get_title() == "Temperature Trend"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_xdata().shape == (7,)
    assert ax.get_lines()[0].get_ydata().shape == (7,)