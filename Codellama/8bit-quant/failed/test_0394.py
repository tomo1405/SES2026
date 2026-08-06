import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test 1: Check that the function returns a matplotlib figure object
    fig = task_func(mu=0, sigma=1)
    assert isinstance(fig, plt.Figure)

    # Test 2: Check that the function plots a histogram with the correct number of bins
    fig = task_func(mu=0, sigma=1, num_samples=1000)
    ax = fig.axes[0]
    assert len(ax.patches) == 30

    # Test 3: Check that the function plots a probability plot with the correct distribution
    fig = task_func(mu=0, sigma=1, num_samples=1000)
    ax = fig.axes[1]
    assert ax.get_title() == "Probability Plot"
    assert ax.get_xlabel() == "Sample Values"
    assert ax.get_ylabel() == "Theoretical Quantiles"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

    # Test 4: Check that the function raises a ValueError if the number of samples is too small
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, num_samples=10)

    # Test 5: Check that the function raises a ValueError if the seed is not an integer
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, seed="abc")