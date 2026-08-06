python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pytest

def task_func(length):

    MU = 0
    SIGMA = 1
    
    distribution = np.random.normal(MU, SIGMA, length)
    fig, ax = plt.subplots()
    ax.hist(distribution, 30, density=True, label='Histogram')
    ax.plot(np.sort(distribution), norm.pdf(np.sort(distribution), MU, SIGMA), 
            linewidth=2, color='r', label='PDF')
    ax.legend()
    
    return distribution, ax

def test_task_func():
    # Test case 1: length = 100
    distribution, ax = task_func(100)
    assert len(distribution) == 100
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Values'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_title() == 'Histogram and PDF of Normal Distribution'
    assert ax.get_xlim() == (-3.5, 3.5)
    assert ax.get_ylim() == (0, 0.45)
    assert ax.get_legend().get_texts()[0].get_text() == 'Histogram'
    assert ax.get_legend().get_texts()[1].get_text() == 'PDF'
    
    # Test case 2: length = 500
    distribution, ax = task_func(500)
    assert len(distribution) == 500
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Values'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_title() == 'Histogram and PDF of Normal Distribution'
    assert ax.get_xlim() == (-3.5, 3.5)
    assert ax.get_ylim() == (0, 0.04)
    assert ax.get_legend().get_texts()[0].get_text() == 'Histogram'
    assert ax.get_legend().get_texts()[1].get_text() == 'PDF'