import pytest
from src_0218 import task_func
import numpy as np

def test_task_func_default_parameters():
    ax, mean, std = task_func()
    assert mean == pytest.approx(0, abs=1e-6)
    assert std == pytest.approx(1, abs=1e-6)

def test_task_func_custom_parameters():
    mu = 5
    sigma = 2
    ax, mean, std = task_func(mu=mu, sigma=sigma)
    assert mean == pytest.approx(mu, abs=1e-6)
    assert std == pytest.approx(sigma, abs=1e-6)

def test_task_func_sample_size():
    sample_size = 2000
    ax, _, _ = task_func(sample_size=sample_size)
    assert len(ax.patches) == 30  # Number of bins in the histogram

def test_task_func_seed():
    ax1, mean1, std1 = task_func(seed=42)
    ax2, mean2, std2 = task_func(seed=42)
    assert mean1 == pytest.approx(mean2, abs=1e-6)
    assert std1 == pytest.approx(std2, abs=1e-6)