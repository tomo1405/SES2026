import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from src_0983 import task_func


def test_task_func():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 1000), "B": np.random.normal(0, 1, 1000)})
    column = "A"
    bins = 30
    density = True
    alpha = 0.6
    color = "g"
    seed = None

    ax = task_func(df, column, bins, density, alpha, color, seed)

    assert ax.get_title() == f"Normal Fit for '{column}'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == column
    assert ax.get_xlim() == (xmin, xmax)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "k"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == color
    assert ax.get_lines()[1].get_linewidth() == 2

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    assert np.allclose(ax.get_lines()[0].get_ydata(), p)

    plt.close()