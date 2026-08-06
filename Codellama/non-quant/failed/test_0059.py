import pytest
from src_0059 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: mu = 0, sigma = 1, num_samples = 100
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
    assert np.allclose(fig.axes[0].get_lines()[0].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[0].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))
    assert np.allclose(fig.axes[0].get_lines()[1].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[1].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))

    # Test case 2: mu = 10, sigma = 2, num_samples = 50
    mu = 10
    sigma = 2
    num_samples = 50
    fig = task_func(mu, sigma, num_samples)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Normal Distribution'
    assert len(fig.axes[0].get_lines()) == 2
    assert fig.axes[0].get_lines()[0].get_color() == 'g'
    assert fig.axes[0].get_lines()[1].get_color() == 'k'
    assert fig.axes[0].get_lines()[1].get_linewidth() == 2
    assert np.allclose(fig.axes[0].get_lines()[0].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[0].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))
    assert np.allclose(fig.axes[0].get_lines()[1].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[1].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))

    # Test case 3: mu = -5, sigma = 1.5, num_samples = 200
    mu = -5
    sigma = 1.5
    num_samples = 200
    fig = task_func(mu, sigma, num_samples)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Normal Distribution'
    assert len(fig.axes[0].get_lines()) == 2
    assert fig.axes[0].get_lines()[0].get_color() == 'g'
    assert fig.axes[0].get_lines()[1].get_color() == 'k'
    assert fig.axes[0].get_lines()[1].get_linewidth() == 2
    assert np.allclose(fig.axes[0].get_lines()[0].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[0].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))
    assert np.allclose(fig.axes[0].get_lines()[1].get_xdata(), np.linspace(mu - 3*sigma, mu + 3*sigma, 100))
    assert np.allclose(fig.axes[0].get_lines()[1].get_ydata(), stats.norm.pdf(np.linspace(mu - 3*sigma, mu + 3*sigma, 100), mu, sigma))