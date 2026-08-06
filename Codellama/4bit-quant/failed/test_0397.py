import pytest
from src_0397 import task_func

def test_task_func():
    # Test that the function raises an error when sample_size is <= 0
    with pytest.raises(ValueError):
        task_func(0, 1, 0)

    # Test that the function returns a valid matplotlib Axes object
    ax = task_func(0, 1, 10)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function plots the correct data
    x = np.linspace(min(sample), max(sample), sample_size)
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), density(x))