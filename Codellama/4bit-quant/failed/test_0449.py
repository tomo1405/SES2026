import pytest
from src_0449 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    mu = 0
    sigma = 1
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    assert np.allclose(ax.get_xlim(), (mu - 3 * sigma, mu + 3 * sigma))
    assert np.allclose(ax.get_ylim(), (0, 1))
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Normal Distribution'

    plt.close(fig)