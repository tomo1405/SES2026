import pytest
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

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
    x = [np.linspace(0, 10, 100) for _ in range(3)]
    y = [np.exp(-0.1*xi) + np.random.normal(0, 0.1, 100) for xi in x]
    labels = ['data1', 'data2', 'data3']
    fig = task_func(x, y, labels)
    assert fig is not None
    assert len(fig.axes) == 1
    assert len(fig.axes[0].get_legend_handles_labels()[0]) == 3

def test_task_func_empty_data():
    x = [[] for _ in range(3)]
    y = [[] for _ in range(3)]
    labels = ['data1', 'data2', 'data3']
    with pytest.raises(ValueError):
        task_func(x, y, labels)