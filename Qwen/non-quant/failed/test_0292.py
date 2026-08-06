import pytest
from src_0292 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup_teardown():
    # Setup: Save the current state of the matplotlib figure
    original_fig = plt.gcf()
    original_ax = plt.gca()

    yield

    # Teardown: Restore the original state of the matplotlib figure
    plt.close('all')
    plt.figure(original_fig.number)
    plt.sca(original_ax)

def test_task_func(setup_teardown):
    mu = 0
    sigma = 1
    result = task_func(mu, sigma)

    # Check if the result is a matplotlib collection
    assert isinstance(result, plt.AxesImage)

    # Check if the plot has the correct number of samples
    ax = plt.gca()
    lines = ax.get_lines()
    assert len(lines) == 1

    # Check if the plot has a colorbar
    colorbars = ax.figure.axes
    assert any(isinstance(cbar, plt.Axes) and cbar.has_data() for cbar in colorbars)

    # Check if the samples have the correct mean and standard deviation
    samples = result.get_array().data
    assert np.isclose(np.mean(samples), mu, atol=0.1)
    assert np.isclose(np.std(samples), sigma, atol=0.1)