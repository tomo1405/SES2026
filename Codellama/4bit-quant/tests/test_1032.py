import matplotlib
import pytest
from src_1032 import task_func


def test_task_func():
    # Test that the function raises an error when n_rows is not positive
    with pytest.raises(ValueError):
        task_func(n_rows=0)

    # Test that the function returns a valid plot when n_rows is positive
    ax = task_func(n_rows=1000)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"
    assert ax.get_xlabel() == "String"
    assert ax.get_ylabel() == "Frequency"