import pytest
from src_0095 import task_func
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

@pytest.fixture
def setup_data():
    mean = 0
    std_dev = 1
    num_samples = 1000
    return mean, std_dev, num_samples

def test_task_func_return_types(setup_data):
    mean, std_dev, num_samples = setup_data
    samples, fig = task_func(mean, std_dev, num_samples)
    assert isinstance(samples, np.ndarray)
    assert isinstance(fig, plt.Figure)

def test_task_func_sample_properties(setup_data):
    mean, std_dev, num_samples = setup_data
    samples, _ = task_func(mean, std_dev, num_samples)
    assert len(samples) == num_samples
    assert np.isclose(np.mean(samples), mean, atol=0.1)
    assert np.isclose(np.std(samples), std_dev, atol=0.1)

def test_task_func_plot(setup_data):
    mean, std_dev, num_samples = setup_data
    _, fig = task_func(mean, std_dev, num_samples)
    ax = fig.axes[0]
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    assert np.allclose(ax.lines[0].get_ydata(), p, atol=0.1)
    assert ax.get_title() == f"Fit results: mean = {mean:.2f},  std = {std_dev:.2f}"