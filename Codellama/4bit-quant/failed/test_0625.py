import pytest
from src_0625 import task_func
import numpy as np

def test_task_func():
    L = [1, 2, 3, 4, 5]
    pca_result, ax = task_func(L)
    assert isinstance(pca_result, np.ndarray)
    assert pca_result.shape == (len(L), N_COMPONENTS)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'Principal component 1'
    assert ax.get_ylabel() == 'Principal component 2'