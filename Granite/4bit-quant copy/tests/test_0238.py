import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from src_0238 import task_func
import pytest

def test_task_func():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path="test.png")
    assert isinstance(coordinates_2d, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_without_plot_path():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True)