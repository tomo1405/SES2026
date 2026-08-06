import pytest
from src_0475 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func_default_values():
    ax, samples = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(samples, np.ndarray)
    assert len(samples) == 1000
    assert np.isclose(np.mean(samples), 0, atol=0.1)
    assert np.isclose(np.std(samples), 1, atol=0.1)

def test_task_func_custom_values():
    ax, samples = task_func(n_samples=500, mu=5, sigma=2, random_seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(samples, np.ndarray)
    assert len(samples) == 500
    assert np.isclose(np.mean(samples), 5, atol=0.1)
    assert np.isclose(np.std(samples), 2, atol=0.1)

def test_task_func_invalid_n_samples():
    with pytest.raises(ValueError, match="Invalid n_samples or sigma"):
        task_func(n_samples=-100)

def test_task_func_invalid_sigma():
    with pytest.raises(ValueError, match="Invalid n_samples or sigma"):
        task_func(sigma=-1)

def test_task_func_no_plot_display():
    ax, samples = task_func()
    plt.ioff()  # Turn off interactive mode to prevent plot display
    plt.show()  # This should not cause any issues