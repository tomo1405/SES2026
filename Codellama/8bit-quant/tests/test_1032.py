import matplotlib
import pytest
from src_1032 import task_func


def test_task_func_positive_n_rows():
    n_rows = 1000
    ax = task_func(n_rows)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"
    assert ax.get_xlabel() == "String"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_negative_n_rows():
    n_rows = -1000
    with pytest.raises(ValueError):
        task_func(n_rows)