import pytest
from src_0095 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    mean = 0
    std_dev = 1
    num_samples = 1000

    samples, fig = task_func(mean, std_dev, num_samples)

    assert isinstance(samples, np.ndarray), "The samples should be a numpy array"
    assert len(samples) == num_samples, "The number of samples should be equal to num_samples"

    assert isinstance(fig, plt.Figure), "The figure should be a matplotlib figure"

    # Additional assertions to check the histogram and the fitted normal distribution
    assert plt.gcf() == fig, "The figure should be the current figure"
    assert len(plt.get_fignums()) == 1, "There should be exactly one figure"

    # Additional checks can be added to ensure the histogram and the fitted normal distribution are correct

pytest.main()