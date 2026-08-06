import pytest
from src_0582 import task_func

def test_task_func():
    # Test that the function returns a matplotlib.axes.Axes object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function plots the correct data
    x_values = np.arange(0, SIZE)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(SIZE)]
    assert np.allclose(ax.get_xdata(), x_values)
    assert np.allclose(ax.get_ydata(), y_values)

    # Test that the function plots the correct title
    assert ax.get_title() == "Sine Wave"

    # Test that the function plots the correct x-axis label
    assert ax.get_xlabel() == "X-Axis"

    # Test that the function plots the correct y-axis label
    assert ax.get_ylabel() == "Y-Axis"