import pytest
from src_0625 import task_func
import numpy as np

def test_task_func():
    L = [1, 2, 3, 4, 5]
    pca_result, ax = task_func(L)

    assert isinstance(pca_result, np.ndarray)
    assert pca_result.shape == (5, 2)

    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'

    assert ax.get_title() == 'PCA of L'
    assert ax.get_xlim() == (-1, 1)
    assert ax.get_ylim() == (-1, 1)

    assert ax.get_xticks() == np.arange(-1, 1.1, 0.5)
    assert ax.get_yticks() == np.arange(-1, 1.1, 0.5)

    assert ax.get_xticklabels() == ['-1', '-0.5', '0', '0.5', '1']
    assert ax.get_yticklabels() == ['-1', '-0.5', '0', '0.5', '1']