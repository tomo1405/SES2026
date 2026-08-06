import pytest
from src_0449 import task_func

def test_task_func():
    # Test that the function returns a matplotlib axis object
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function plots the normal distribution
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)
    assert np.allclose(ax.get_ydata(), y)

    # Test that the function sets the correct x-axis limits
    assert ax.get_xlim() == (mu - 3 * sigma, mu + 3 * sigma)

    # Test that the function sets the correct y-axis limits
    assert ax.get_ylim() == (0, 1)