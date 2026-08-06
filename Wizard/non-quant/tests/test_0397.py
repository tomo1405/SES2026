python
import pytest
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from src_0397 import task_func

def test_task_func():
    # Test case 1: sample_size is a positive integer
    mu = 0
    sigma = 1
    sample_size = 100
    seed = 0
    ax = task_func(mu, sigma, sample_size, seed)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Gaussian KDE'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Density'
    assert len(ax.lines) == 1
    assert ax.lines[0].get_color() == 'black'
    assert ax.lines[0].get_linestyle() == '-'
    assert ax.lines[0].get_linewidth() == 1.0
    assert ax.lines[0].get_alpha() == 1.0
    assert ax.lines[0].get_marker() == 'None'
    assert ax.lines[0].get_markersize() == 1.0
    assert ax.lines[0].get_markeredgewidth() == 1.0
    assert ax.lines[0].get_markerfacecolor() == 'None'
    assert ax.lines[0].get_markeredgecolor() == 'None'
    assert ax.lines[0].get_xdata().shape == (100,)
    assert ax.lines[0].get_ydata().shape == (100,)
    assert ax.lines[0].get_ydata().min() >= 0.0
    assert ax.lines[0].get_ydata().max() <= 1.0
    assert ax.lines[0].get_ydata().mean() == pytest.approx(0.5, abs=0.1)
    assert ax.lines[0].get_xdata().min() == pytest.approx(-3.0, abs=0.1)
    assert ax.lines[0].get_xdata().max() == pytest.approx(3.0, abs=0.1)

    # Test case 2: sample_size is zero
    mu = 0
    sigma = 1
    sample_size = 0
    seed = 0
    with pytest.raises(ValueError):
        ax = task_func(mu, sigma, sample_size, seed)

    # Test case 3: sample_size is negative
    mu = 0
    sigma = 1
    sample_size = -100
    seed = 0
    with pytest.raises(ValueError):
        ax = task_func(mu, sigma, sample_size, seed)