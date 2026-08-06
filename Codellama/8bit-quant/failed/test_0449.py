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

    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Normal Distribution'
    assert ax.get_xlim() == (mu - 3 * sigma, mu + 3 * sigma)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == np.linspace(mu - 3 * sigma, mu + 3 * sigma, 10)
    assert ax.get_yticks() == np.linspace(0, 1, 10)
    assert ax.get_xticklabels() == ['{:.2f}'.format(x) for x in np.linspace(mu - 3 * sigma, mu + 3 * sigma, 10)]
    assert ax.get_yticklabels() == ['{:.2f}'.format(y) for y in np.linspace(0, 1, 10)]