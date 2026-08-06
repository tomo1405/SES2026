python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pytest

def task_func(x, y, labels):
    pca = PCA(n_components=2)

    fig, ax = plt.subplots()

    for i in range(len(x)):
        xy = np.vstack((x[i], y[i])).T
        xy_transformed = pca.fit_transform(xy)
        ax.plot(xy_transformed[:, 0], xy_transformed[:, 1], label=labels[i])
    
    ax.legend()
    
    return fig

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['A', 'B']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert isinstance(fig.axes[0], plt.Axes)
    assert len(fig.axes[0].lines) == 2
    assert fig.axes[0].lines[0].get_label() == 'A'
    assert fig.axes[0].lines[1].get_label() == 'B'