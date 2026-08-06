import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def test_task_func():
    # Define a simple function to use in the test
    def test_func(x):
        return np.sin(x)

    # Call the function with default parameters
    ax = task_func(test_func)

    # Check that the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes)

    # Check that the plot contains two lines: one for the function and one for its integral
    lines = ax.get_lines()
    assert len(lines) == 2

    # Check the labels of the lines
    assert lines[0].get_label() == "test_func(x)"
    assert lines[1].get_label() == "Integral of test_func(x)"

    # Check the data plotted on the axes
    X = np.linspace(-2, 2, 1000)
    y = np.sin(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)

    np.testing.assert_array_almost_equal(ax.lines[0].get_ydata(), y)
    np.testing.assert_array_almost_equal(ax.lines[1].get_ydata(), y_int)

# Run the tests
if __name__ == "__main__":
    pytest.main()