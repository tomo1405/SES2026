python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pytest

def task_func(mu, sigma, num_samples=1000, seed=77):
    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    fig = plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    plt.subplot(1, 2, 2)
    stats.probplot(samples, dist="norm", plot=plt)

    return fig

def test_task_func():
    # Test case 1: Check if the function returns a matplotlib figure object
    fig = task_func(0, 1)
    assert isinstance(fig, plt.Figure)

    # Test case 2: Check if the function returns a figure with 2 subplots
    assert len(fig.axes) == 2

    # Test case 3: Check if the function returns a figure with a normal distribution plot in the first subplot
    assert fig.axes[0].get_title() == 'Normal probability plot'

    # Test case 4: Check if the function returns a figure with a histogram plot in the second subplot
    assert fig.axes[1].get_title() == 'Histogram'

    # Test case 5: Check if the function returns a figure with a normal distribution plot in the first subplot
    assert fig.axes[0].lines[0].get_color() == 'g'

    # Test case 6: Check if the function returns a figure with a normal distribution plot in the first subplot
    assert fig.axes[1].patches[0].get_facecolor() == (0.3, 0.3, 0.3, 1.0)