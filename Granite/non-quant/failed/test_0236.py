import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import pytest

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a histogram and get the Axes object
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, num_bins, density=True)
    ax.plot(
        bins, 
        1/(sigma * np.sqrt(2 * np.pi)) * \
        np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r'
    )
    bins = (bins[:-1] + bins[1:]) / 2
    model = ols('count ~ bins + np.power(bins, 2)', data={'count': count, 'bins': bins}).fit()
    ax.plot(
        bins, 
        model.params['Intercept'] + model.params['bins'] * bins + \
        model.params['np.power(bins, 2)'] * np.power(bins, 2), linewidth=2, color='g'
    )
    
    return ax

def test_task_func():
    ax = task_func(mu=0, sigma=1, seed=0, num_samples=1000, num_bins=30)
    assert ax is not None
    assert ax.get_title() == 'Histogram of 1000 samples from N(0, 1)'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Density'
    assert len(ax.patches) == 30
    assert ax.lines[0].get_color() == 'r'
    assert ax.lines[1].get_color() == 'g'