import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain
def task_func(L):
    data = list(chain(*L))
    mu, std = norm.fit(data)

    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    ax.set_title(title)

    return ax
import pytest
def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Fit results: mu = 5.00,  std = 2.87"
def test_task_func_with_empty_list():
    L = [[]]
    with pytest.raises(ValueError):
        task_func(L)
def test_task_func_with_non_list():
    L = 123
    with pytest.raises(TypeError):
        task_func(L)