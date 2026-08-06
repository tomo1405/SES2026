import pytest
from src_0968 import task_func
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import io

# Mocking plt to capture plot output
class MockPlot:
    def __init__(self):
        self.figures = []

    def subplots(self):
        fig, ax = plt.subplots()
        self.figures.append((fig, ax))
        return fig, ax

    def savefig(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_plot(monkeypatch):
    mock = MockPlot()
    monkeypatch.setattr(plt, 'subplots', mock.subplots)
    monkeypatch.setattr(plt, 'savefig', mock.savefig)
    return mock

def test_task_func(mock_plot):
    # Define a simple function to test
    def test_func(x):
        return np.sin(x)

    # Call the function with default parameters
    ax = task_func(test_func)

    # Check that the correct number of figures were created
    assert len(mock_plot.figures) == 1

    # Extract the figure and axis
    fig, ax = mock_plot.figures[0]

    # Check that the correct labels were set
    lines = ax.get_lines()
    assert lines[0].get_label() == "test_func(x)"
    assert lines[1].get_label() == "Integral of test_func(x)"

    # Check that the data is plotted correctly
    X = np.linspace(-2, 2, 1000)
    y = test_func(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)
    np.testing.assert_array_almost_equal(lines[0].get_ydata(), y)
    np.testing.assert_array_almost_equal(lines[1].get_ydata(), y_int)

    # Check that the legend is present
    assert ax.get_legend() is not None

# Test with custom parameters
def test_task_func_custom_params(mock_plot):
    # Define a simple function to test
    def test_func(x):
        return x**2

    # Call the function with custom parameters
    ax = task_func(test_func, x_range=(0, 5), num_points=500)

    # Check that the correct number of figures were created
    assert len(mock_plot.figures) == 1

    # Extract the figure and axis
    fig, ax = mock_plot.figures[0]

    # Check that the correct labels were set
    lines = ax.get_lines()
    assert lines[0].get_label() == "test_func(x)"
    assert lines[1].get_label() == "Integral of test_func(x)"

    # Check that the data is plotted correctly
    X = np.linspace(0, 5, 500)
    y = test_func(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)
    np.testing.assert_array_almost_equal(lines[0].get_ydata(), y)
    np.testing.assert_array_almost_equal(lines[1].get_ydata(), y_int)

    # Check that the legend is present
    assert ax.get_legend() is not None