import numpy as np
from src_0218 import task_func


def test_task_func():
    # Test with default parameters
    ax, mean, std = task_func()
    assert np.isclose(mean, 0)
    assert np.isclose(std, 1)
    assert ax.get_title() == "Normal Distribution with $\\mu = 0, \\sigma = 1$"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_legend() == "Sample Histogram"
    assert ax.get_legend() == "Normal PDF"

    # Test with custom parameters
    ax, mean, std = task_func(mu=1, sigma=2, sample_size=1000, seed=0)
    assert np.isclose(mean, 1)
    assert np.isclose(std, 2)
    assert ax.get_title() == "Normal Distribution with $\\mu = 1, \\sigma = 2$"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_legend() == "Sample Histogram"
    assert ax.get_legend() == "Normal PDF"