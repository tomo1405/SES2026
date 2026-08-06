python
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
    # Test case 1: Test with default values
    ax = task_func(0, 1)
    assert ax.get_title() == 'Normal Distribution'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Density'
    assert len(ax.lines) == 2
    assert ax.lines[0].get_color() == 'r'
    assert ax.lines[1].get_color() == 'g'
    assert ax.lines[0].get_label() == 'Normal Distribution'
    assert ax.lines[1].get_label() == 'Normal Distribution Fit'
    assert ax.get_xlim() == (-3.5, 3.5)
    assert ax.get_ylim() == (0, 0.45)
    
    # Test case 2: Test with custom values
    ax = task_func(2, 3, seed=1, num_samples=100, num_bins=20)
    assert ax.get_title() == 'Normal Distribution'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Density'
    assert len(ax.lines) == 2
    assert ax.lines[0].get_color() == 'r'
    assert ax.lines[1].get_color() == 'g'
    assert ax.lines[0].get_label() == 'Normal Distribution'
    assert ax.lines[1].get_label() == 'Normal Distribution Fit'
    assert ax.get_xlim() == (0.5, 4.5)
    assert ax.get_ylim() == (0, 0.06)
    
    # Test case 3: Test with invalid values
    with pytest.raises(ValueError):
        task_func(0, -1)
    with pytest.raises(ValueError):
        task_func(0, 1, num_samples=-1)
    with pytest.raises(ValueError):
        task_func(0, 1, num_bins=-1)