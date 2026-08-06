import pytest
from src_0236 import task_func
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def test_task_func():
    # Test with default parameters
    ax = task_func(mu=0, sigma=1)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_xlabel() == 'bins'
    assert ax.get_ylabel() == 'count'
    assert ax.get_title() == 'Histogram of Normal Distribution'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_color() == 'r'
    assert ax.get_lines()[1].get_color() == 'g'

    # Test with custom parameters
    ax = task_func(mu=1, sigma=2, seed=123, num_samples=500, num_bins=50)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_xlabel() == 'bins'
    assert ax.get_ylabel() == 'count'
    assert ax.get_title() == 'Histogram of Normal Distribution'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_color() == 'r'
    assert ax.get_lines()[1].get_color() == 'g'

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(mu=1, sigma=0)
    with pytest.raises(ValueError):
        task_func(mu=1, sigma=-1)
    with pytest.raises(ValueError):
        task_func(mu=1, sigma=1, seed=-1)
    with pytest.raises(ValueError):
        task_func(mu=1, sigma=1, num_samples=-1)
    with pytest.raises(ValueError):
        task_func(mu=1, sigma=1, num_bins=-1)