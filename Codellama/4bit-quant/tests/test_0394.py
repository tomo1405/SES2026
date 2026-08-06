import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test 1: Check if the function returns a figure object
    fig = task_func(0, 1)
    assert isinstance(fig, plt.Figure)

    # Test 2: Check if the function plots a histogram
    fig = task_func(0, 1)
    ax = fig.axes[0]
    assert ax.get_title() == "Histogram"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"

    # Test 3: Check if the function plots a probability plot
    fig = task_func(0, 1)
    ax = fig.axes[1]
    assert ax.get_title() == "Probability Plot"
    assert ax.get_xlabel() == "Sample Values"
    assert ax.get_ylabel() == "Theoretical Quantiles"

    # Test 4: Check if the function raises an error when the input is invalid
    with pytest.raises(ValueError):
        task_func(0, -1)