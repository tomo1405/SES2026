import pytest
from src_0225 import task_func

def test_task_func():
    # Test that the function raises a ValueError when range_start is smaller than range_end
    with pytest.raises(ValueError):
        task_func(range_start=-10, range_end=10, step=0.1)

    # Test that the function returns the correct data and axes
    data, ax, mean, median = task_func(range_start=0, range_end=10, step=0.1)
    assert isinstance(data, tuple)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(mean, float)
    assert isinstance(median, float)

    # Test that the function plots the correct data
    assert len(ax.lines) == 3
    assert ax.lines[0].get_color() == 'b'
    assert ax.lines[1].get_color() == 'r'
    assert ax.lines[2].get_color() == 'g'

    # Test that the function calculates the correct mean and median
    assert mean == pytest.approx(0.0)
    assert median == pytest.approx(0.0)