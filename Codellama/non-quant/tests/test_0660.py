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
    for i in range(3):
        assert ax.lines[i].get_label() == labels[i]
        assert ax.lines[i].get_xdata() == x
        assert ax.lines[i].get_ydata() == stats.norm.pdf(x, np.mean(y[i]), np.std(y[i]))

    assert ax.get_legend() is not None
    assert ax.get_legend().get_texts() == labels