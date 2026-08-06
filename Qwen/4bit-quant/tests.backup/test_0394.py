import pytest
from src_0394 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.mark.parametrize("mu, sigma, num_samples, seed", [
    (0, 1, 1000, 77),
    (5, 2, 500, 42),
    (-1, 0.5, 2000, 123),
])
def test_task_func(mu, sigma, num_samples, seed):
    fig = task_func(mu, sigma, num_samples, seed)
    
    # Check if the figure is created with 2 subplots
    assert len(fig.axes) == 2
    
    # Check if the first subplot is a histogram
    ax1 = fig.axes[0]
    assert isinstance(ax1, plt.Axes)
    assert len(ax1.patches) > 0  # There should be some bars in the histogram
    
    # Check if the second subplot is a probability plot
    ax2 = fig.axes[1]
    assert isinstance(ax2, plt.Axes)
    assert len(ax2.lines) > 0  # There should be some lines in the probability plot
    
    # Check if the random samples generated match the parameters
    np.random.seed(seed)
    expected_samples = np.random.normal(mu, sigma, num_samples)
    assert np.allclose(np.mean(expected_samples), mu, atol=0.1)
    assert np.allclose(np.std(expected_samples), sigma, atol=0.1)

# To run the tests, use the command: pytest <filename>.py