import pytest
from src_0095 import task_func
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def test_task_func():
    # Test with valid inputs
    mean = 0
    std_dev = 1
    num_samples = 100
    samples, fig = task_func(mean, std_dev, num_samples)
    assert isinstance(samples, np.ndarray)
    assert samples.shape == (num_samples,)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_xlim() == (0, 1)
    assert fig.axes[0].get_ylim() == (0, 1)
    assert fig.axes[0].get_title() == "Fit results: mean = 0.00,  std = 1.00"

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(mean, std_dev, num_samples, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(mean, std_dev, num_samples, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(mean, std_dev, num_samples, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(mean, std_dev, num_samples, invalid_arg=True)