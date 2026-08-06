import matplotlib.pyplot as plt
import numpy as np
from src_0370 import task_func


def test_task_func():
    l = np.random.normal(size=100)
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    assert np.allclose(ax.get_xlim(), (xmin, xmax))
    assert np.allclose(ax.get_ylim(), (0, 1))
    assert np.allclose(ax.get_xdata(), x)
    assert np.allclose(ax.get_ydata(), p)