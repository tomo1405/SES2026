import pytest
from src_0376 import task_func
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    l = [[1, 2], [3, 4], [5, 6]]
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'First Principal Component'
    assert ax.get_ylabel() == 'Second Principal Component'
    assert ax.get_title() == 'PCA Result'
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_xdata() == [1, 3, 5]
    assert ax.get_lines()[0].get_ydata() == [2, 4, 6]