import matplotlib
import numpy
import numpy as np
import pytest
from src_0475 import task_func


def test_task_func():
    # Test with valid inputs
    ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=0)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(samples, numpy.ndarray)
    assert samples.shape == (1000,)
    assert np.all(samples >= 0)
    assert np.all(samples <= 1)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(n_samples=0, mu=0, sigma=1, random_seed=0)
    with pytest.raises(ValueError):
        task_func(n_samples=1000, mu=0, sigma=0, random_seed=0)
    with pytest.raises(ValueError):
        task_func(n_samples=1000, mu=0, sigma=1, random_seed=-1)