python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax

def test_task_func():
    ax = task_func()
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Probability density'
    assert ax.get_title() == 'Normal distribution'
    assert ax.get_xlim() == (-3.0, 3.0)
    assert ax.get_ylim() == (0.0, 0.45)