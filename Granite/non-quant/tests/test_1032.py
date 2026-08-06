import matplotlib
import pytest
from src_1032 import task_func


def test_task_func():
    # Test case 1: n_rows is positive
    ax = task_func(n_rows=1000)
    assert ax is not None

    # Test case 2: n_rows is not positive
    with pytest.raises(ValueError):
        task_func(n_rows=0)

    # Test case 3: Check the type of the returned object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 4: Check the title of the plot
    ax = task_func(n_rows=1000)
    assert ax.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"

    # Test case 5: Check the x-label of the plot
    ax = task_func(n_rows=1000)
    assert ax.get_xlabel() == "String"

    # Test case 6: Check the y-label of the plot
    ax = task_func(n_rows=1000)
    assert ax.get_ylabel() == "Frequency"