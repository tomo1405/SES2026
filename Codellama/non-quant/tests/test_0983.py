import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from src_0983 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    bins = 30
    density = True
    alpha = 0.6
    color = 'g'
    seed = None

    ax = task_func(df, column, bins, density, alpha, color, seed)

    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == f"Normal Fit for '{column}'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == column

    data = df[column]
    mu, std = norm.fit(data)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)

    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), p)

    assert ax.lines[0].get_color() == 'k'
    assert ax.lines[0].get_linewidth() == 2

    assert ax.get_xlim() == (xmin, xmax)
    assert ax.get_ylim() == (0, 1)

    assert ax.get_xticks() == np.linspace(xmin, xmax, 11)
    assert ax.get_yticks() == np.linspace(0, 1, 11)