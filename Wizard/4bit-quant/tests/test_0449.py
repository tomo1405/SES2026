python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pytest

def task_func(mu=0, sigma=1):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert ax.lines[0].get_data()[0].shape == (100,)
    assert ax.lines[0].get_data()[1].shape == (100,)