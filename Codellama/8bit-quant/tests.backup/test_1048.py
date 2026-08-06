import pytest
from src_1048 import task_func

def test_task_func():
    date_str = "2023-02-28"
    ax = task_func(date_str)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Day"
    assert ax.get_ylabel() == "Random Values"
    assert ax.get_title() == "Random Values for 28th February 2023"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Random Values"
    assert ax.get_lines()[0].get_color() == "blue"
    assert ax.get_lines()[0].get_linestyle() == "-"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[0].get_marker() == "o"
    assert ax.get_lines()[0].get_markerfacecolor() == "red"
    assert ax.get_lines()[0].get_markeredgecolor() == "black"
    assert ax.get_lines()[0].get_markersize() == 10