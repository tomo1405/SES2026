import pytest
from src_0663 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    labels = ['label1', 'label2']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert fig.axes[0].get_legend() is not None
    assert fig.axes[0].get_legend().get_texts()[0].get_text() == 'label1'
    assert fig.axes[0].get_legend().get_texts()[1].get_text() == 'label2'

    xy = np.vstack((x[0], y[0])).T
    xy_transformed = PCA(n_components=2).fit_transform(xy)
    assert np.allclose(fig.axes[0].get_lines()[0].get_xydata(), xy_transformed)

    xy = np.vstack((x[1], y[1])).T
    xy_transformed = PCA(n_components=2).fit_transform(xy)
    assert np.allclose(fig.axes[0].get_lines()[1].get_xydata(), xy_transformed)