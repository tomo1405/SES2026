import pytest
from src_0236 import task_func
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def test_task_func():
    # Test with default parameters
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_xlabel() == 'Bins'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Histogram of Normal Distribution'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_color() == 'r'
    assert ax.get_lines()[1].get_color() == 'g'

    # Test with custom parameters
    ax = task_func(mu=10, sigma=2, seed=123, num_samples=500, num_bins=20)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_xlabel() == 'Bins'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Histogram of Normal Distribution'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_color() == 'r'
    assert ax.get_lines()[1].get_color() == 'g'

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(mu=10, sigma=0)
    with pytest.raises(ValueError):
        task_func(mu=10, sigma=-1)
    with pytest.raises(ValueError):
        task_func(mu=10, sigma=2, seed=-1)
    with pytest.raises(ValueError):
        task_func(mu=10, sigma=2, num_samples=-1)
    with pytest.raises(ValueError):
        task_func(mu=10, sigma=2, num_bins=-1)