import pytest
from src_0383 import task_func
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

@pytest.fixture
def setup_environment():
    plt.switch_backend('Agg')  # Use a non-interactive backend to avoid GUI issues during tests

def test_task_func_length(setup_environment):
    length = 1000
    distribution, ax = task_func(length)
    assert len(distribution) == length, "The length of the distribution does not match the input length"

def test_task_func_distribution_mean(setup_environment):
    length = 1000
    distribution, _ = task_func(length)
    mean = np.mean(distribution)
    assert np.isclose(mean, 0, atol=0.1), "The mean of the distribution is not close to 0"

def test_task_func_distribution_std(setup_environment):
    length = 1000
    distribution, _ = task_func(length)
    std = np.std(distribution)
    assert np.isclose(std, 1, atol=0.1), "The standard deviation of the distribution is not close to 1"

def test_task_func_plot(setup_environment):
    length = 1000
    _, ax = task_func(length)
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot (histogram and PDF)"
    assert lines[0].get_label() == 'Histogram', "The first line should be labeled 'Histogram'"
    assert lines[1].get_label() == 'PDF', "The second line should be labeled 'PDF'"

def test_task_func_plot_density(setup_environment):
    length = 1000
    _, ax = task_func(length)
    patches = ax.patches
    assert len(patches) == 30, "There should be 30 bins in the histogram"