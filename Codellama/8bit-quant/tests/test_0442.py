import pytest
from src_0442 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    result, ax = task_func(P, T)
    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 3)
    assert isinstance(ax, plt.Axes3D)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_zlabel() == "z"
    assert ax.get_title() == "3D Visualization"