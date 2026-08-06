import pytest
from src_0468 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    n = 10
    seed = 42
    fig, points = task_func(n, seed)

    # Check if the number of points is correct
    assert len(points) == n

    # Check if the points are within the expected range [0, 1)
    for x, y in points:
        assert 0 <= x < 1
        assert 0 <= y < 1

    # Check if the figure is created correctly
    assert isinstance(fig, plt.Figure)

    # Check if the axes are set correctly
    ax = fig.axes[0]
    assert ax.get_title() == "Scatter plot of random points"
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"

    # Check if the scatter plot contains the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1
    assert len(lines[0].get_xdata()) == n
    assert len(lines[0].get_ydata()) == n

# Run the test
if __name__ == "__main__":
    pytest.main()