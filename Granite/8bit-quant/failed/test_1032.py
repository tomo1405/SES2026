import pytest
from src_1032 import task_func

def test_task_func():
    # Test if n_rows is positive
    with pytest.raises(ValueError):
        task_func(n_rows=-1)

    # Test if the function returns a matplotlib Axes object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test if the plot has the correct title, x-label, and y-label
    ax = task_func()
    assert ax.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"
    assert ax.get_xlabel() == "String"
    assert ax.get_ylabel() == "Frequency"