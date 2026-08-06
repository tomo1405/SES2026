import pytest
from src_0059 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Check if the function returns a figure object
    fig = task_func(0, 1, 100)
    assert isinstance(fig, plt.Figure)

    # Test 2: Check if the function plots a histogram
    ax = fig.axes[0]
    assert ax.get_title() == 'Normal Distribution'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

    # Test 3: Check if the function plots a normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, 0, 1)
    assert np.allclose(ax.lines[0].get_ydata(), p)

    # Test 4: Check if the function sets the correct x-axis limits
    assert ax.get_xlim() == (0, 1)

    # Test 5: Check if the function sets the correct y-axis limits
    assert ax.get_ylim() == (0, 1)

    # Test 6: Check if the function sets the correct title
    assert ax.get_title() == 'Normal Distribution'

    # Test 7: Check if the function sets the correct x-label
    assert ax.get_xlabel() == 'Value'

    # Test 8: Check if the function sets the correct y-label
    assert ax.get_ylabel() == 'Frequency'

    # Test 9: Check if the function sets the correct alpha value
    assert ax.get_alpha() == 0.6

    # Test 10: Check if the function sets the correct linewidth
    assert ax.get_linewidth() == 2