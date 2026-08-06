import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from src_0236 import task_func

def test_task_func():
    mu = 0
    sigma = 1
    seed = 0
    num_samples = 1000
    num_bins = 30
    ax = task_func(mu, sigma, seed, num_samples, num_bins)
    assert isinstance(ax, plt.Axes)

def test_task_func_default_args():
    mu = 0
    sigma = 1
    ax = task_func(mu, sigma)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_args():
    with np.testing.assert_raises(ValueError):
        task_func(0, 0, num_bins='invalid')
    with np.testing.assert_raises(ValueError):
        task_func(0, 0, num_samples=-1)
    with np.testing.assert_raises(ValueError):
        task_func(0, 0, num_bins=0)