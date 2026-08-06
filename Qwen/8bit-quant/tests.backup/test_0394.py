import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    mu = 0
    sigma = 1
    num_samples = 1000
    seed = 77

    # Capture the figure returned by the function
    fig = task_func(mu, sigma, num_samples, seed)

    # Check that the figure is a matplotlib Figure object
    assert isinstance(fig, plt.Figure)

    # Check that the figure has two subplots
    assert len(fig.axes) == 2

    # Check that the first subplot is a histogram
    ax1 = fig.axes[0]
    assert isinstance(ax1, plt.Axes)
    assert 'hist' in [child.get_label() for child in ax1.get_children()]

    # Check that the second subplot is a probability plot
    ax2 = fig.axes[1]
    assert isinstance(ax2, plt.Axes)
    assert 'probplot' in [child.get_label() for child in ax2.get_children()]

    # Check that the random samples have the correct mean and standard deviation
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)
    assert np.isclose(np.mean(samples), mu, atol=0.1)
    assert np.isclose(np.std(samples), sigma, atol=0.1)

    # Check that the histogram data matches the generated samples
    hist_data, _ = np.histogram(samples, bins=30, density=True)
    ax1_data, _ = np.histogram(ax1.patches, bins=30, density=True)
    assert np.allclose(hist_data, ax1_data, atol=0.01)

    # Clean up the plot to avoid displaying it during tests
    plt.close(fig)