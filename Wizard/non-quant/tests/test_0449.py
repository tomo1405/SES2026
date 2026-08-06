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
    assert ax.get_title() == 'Normal Distribution'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'Probability Density'
    assert ax.get_xlim() == (-3.0, 3.0)
    assert ax.get_ylim() == (0.0, 0.45)
    assert ax.get_xticks() == [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]
    assert ax.get_yticks() == [0.0, 0.1, 0.2, 0.3, 0.4]
    assert ax.get_lines()[0].get_data() == (x, y)