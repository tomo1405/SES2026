import matplotlib
import pytest
from src_1032 import task_func


def test_task_func():
    # Test if n_rows is positive
    with pytest.raises(ValueError):
        task_func(n_rows=-1)

    # Test if the function returns the correct type
    assert isinstance(task_func(), matplotlib.axes.Axes)

    # Test if the function returns the correct number of bars
    ax = task_func()
    assert len(ax.patches) == 30