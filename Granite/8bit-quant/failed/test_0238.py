import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from src_0238 import task_func
import pytest

def test_task_func_with_save_plot_true():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    save_plot = True
    plot_path = "plot.png"
    coordinates_2d, ax = task_func(data, save_plot, plot_path)
    assert isinstance(coordinates_2d, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_save_plot_false():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    save_plot = False
    coordinates_2d = task_func(data, save_plot)
    assert isinstance(coordinates_2d, np.ndarray)

def test_task_func_with_save_plot_true_and_no_plot_path():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    save_plot = True
    with pytest.raises(ValueError):
        task_func(data, save_plot)