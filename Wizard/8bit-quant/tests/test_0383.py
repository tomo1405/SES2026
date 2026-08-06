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
    distribution, ax = task_func(1000)
    assert len(distribution) == 1000
    assert isinstance(ax, plt.Axes)