import pytest
from src_0095 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    mean = 0
    std_dev = 1
    num_samples = 1000
    return mean, std_dev, num_samples

def test_task_func_return_type(setup):
    mean, std_dev, num_samples = setup
    samples, fig = task_func(mean, std_dev, num_samples)
    assert isinstance(samples, np.ndarray)
    assert isinstance(fig, plt.Figure)

def test_task_func_samples_length(setup):
    mean, std_dev, num_samples = setup
    samples, _ = task_func(mean, std_dev, num_samples)
    assert len(samples) == num_samples

def test_task_func_samples_mean(setup):
    mean, std_dev, num_samples = setup
    samples, _ = task_func(mean, std_dev, num_samples)
    sample_mean = np.mean(samples)
    assert np.isclose(sample_mean, mean, atol=0.1)

def test_task_func_samples_std(setup):
    mean, std_dev, num_samples = setup
    samples, _ = task_func(mean, std_dev, num_samples)
    sample_std = np.std(samples)
    assert np.isclose(sample_std, std_dev, atol=0.1)

def test_task_func_plot(setup):
    mean, std_dev, num_samples = setup
    _, fig = task_func(mean, std_dev, num_samples)
    ax = fig.axes[0]
    assert len(ax.lines) == 1  # Only one line plot should be added for the PDF
    assert len(ax.patches) > 0  # Histogram should have patches