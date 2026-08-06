import pytest
from src_0059 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    mu = 0
    sigma = 1
    num_samples = 100
    fig = task_func(mu, sigma, num_samples)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Normal Distribution'
    assert len(fig.axes[0].get_lines()) == 2
    assert fig.axes[0].get_lines()[0].get_color() == 'g'
    assert fig.axes[0].get_lines()[1].get_color() == 'k'
    assert fig.axes[0].get_lines()[1].get_linewidth() == 2
    assert np.allclose(fig.axes[0].get_lines()[1].get_ydata(), stats.norm.pdf(np.linspace(0, 10, 100), mu, sigma))