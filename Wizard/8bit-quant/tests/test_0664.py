python
import numpy as np
import pytest
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(x, y, labels):

    if not x or not y or not labels:
        raise ValueError("Empty data lists provided.")

    def exponential_func(x, a, b, c):
        """Exponential function model for curve fitting."""
        return a * np.exp(-b * x) + c

    fig, ax = plt.subplots()

    for i in range(len(x)):
        # Fit the exponential model to the data
        popt, _ = curve_fit(exponential_func, x[i], y[i])

        # Plot the fitted curve
        ax.plot(x[i], exponential_func(x[i], *popt), label=labels[i])

    ax.legend()

    return fig

def test_task_func():
    # Test case 1: Valid input data
    x = [np.arange(10), np.arange(10)]
    y = [np.random.rand(10), np.random.rand(10)]
    labels = ['data1', 'data2']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

    # Test case 2: Empty input data
    x = []
    y = []
    labels = []
    with pytest.raises(ValueError):
        task_func(x, y, labels)

    # Test case 3: Invalid input data
    x = [np.arange(10), np.arange(10)]
    y = [np.random.rand(10), np.random.rand(10)]
    labels = ['data1', 'data2', 'data3']
    with pytest.raises(ValueError):
        task_func(x, y, labels)