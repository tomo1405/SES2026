python
import pytest
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def task_func(mu, sigma, seed=0):
    # Set the random seed
    np.random.seed(seed)
    # Generate samples from the normal distribution
    samples = np.random.normal(mu, sigma, 1000)

    # Generate a KDE plot
    mappable = sns.kdeplot(samples, fill=True)

    # Add a colorbar to the plot
    plt.colorbar(mappable=mappable.collections[0])

    return mappable

def test_task_func():
    # Test case 1: Test with mu=0, sigma=1, seed=0
    mappable = task_func(0, 1, 0)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    assert mappable.get_clim() == (-0.00142578125, 0.00142578125)
    assert mappable.get_array().shape == (1000,)
    assert mappable.get_array().mean() == pytest.approx(0.0, abs=1e-3)
    assert mappable.get_array().std() == pytest.approx(1.0, abs=1e-3)

    # Test case 2: Test with mu=1, sigma=2, seed=1
    mappable = task_func(1, 2, 1)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    assert mappable.get_clim() == (-0.00142578125, 0.00142578125)
    assert mappable.get_array().shape == (1000,)
    assert mappable.get_array().mean() == pytest.approx(1.0, abs=1e-3)
    assert mappable.get_array().std() == pytest.approx(2.0, abs=1e-3)