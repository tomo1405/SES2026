import matplotlib
import pytest
from src_0214 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a matplotlib.axes.Axes object
    ax, kurtosis_value = result
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the second element of the tuple is a float
    assert isinstance(kurtosis_value, float)

    # Test that the function raises a KeyboardInterrupt exception when interrupted
    with pytest.raises(KeyboardInterrupt):
        task_func(intervals=100, seed=0)