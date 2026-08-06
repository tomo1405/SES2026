import pytest
from src_0060 import task_func

def test_task_func():
    # Test that the function returns a valid matplotlib axis object
    ax = task_func("Python (programming language)")
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function raises an exception when the page title is invalid
    with pytest.raises(Exception):
        task_func("Invalid page title")