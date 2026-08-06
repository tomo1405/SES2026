import pytest
from src_0238 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    # Test with valid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path="test_plot.png")
    assert np.allclose(coordinates_2d, [[1, 2], [4, 5], [7, 8]])
    assert isinstance(ax, plt.Axes)

    # Test with invalid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True, plot_path="test_plot.png")

    # Test with invalid plot path
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True, plot_path=None)