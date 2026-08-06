import pytest
from src_0238 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: No save_plot, no plot_path
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    coordinates_2d, ax = task_func(data)
    assert np.allclose(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax

    # Test case 2: save_plot=True, plot_path=None
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True)

    # Test case 3: save_plot=True, plot_path=valid
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    plot_path = "test_plot.png"
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path=plot_path)
    assert np.allclose(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax
    assert os.path.exists(plot_path)
    os.remove(plot_path)