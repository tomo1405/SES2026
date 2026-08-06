import pytest
from src_0660 import task_func
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def test_task_func():
    x = np.array([1, 2, 3])
    y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    labels = ['label1', 'label2', 'label3']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.lines) == 3
    for i in range(len(x)):
        mu = np.mean(y[i])
        sigma = np.std(y[i])
        pdf = stats.norm.pdf(x[i], mu, sigma)
        assert ax.lines[i].get_xdata() == x[i]
        assert ax.lines[i].get_ydata() == pdf
    assert ax.get_legend() == labels