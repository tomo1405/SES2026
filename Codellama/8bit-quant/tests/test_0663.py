import pytest
from src_0663 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[7, 8, 9], [10, 11, 12]])
    labels = ['a', 'b']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert fig.axes[0].get_legend() is not None
    assert fig.axes[0].get_legend().get_texts()[0].get_text() == 'a'
    assert fig.axes[0].get_legend().get_texts()[1].get_text() == 'b'