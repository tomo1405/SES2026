import pytest
from src_0625 import task_func
import numpy as np

def test_task_func():
    L = [1, 2, 3, 4, 5]
    pca_result, ax = task_func(L)

    assert isinstance(pca_result, np.ndarray)
    assert pca_result.shape == (5, 2)
    assert isinstance(ax, plt.Axes)