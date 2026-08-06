import pytest
from src_0238 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    # Test with valid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    coordinates_2d, ax = task_func(data)
    assert np.array_equal(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax

    # Test with invalid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    coordinates_2d, ax = task_func(data, save_plot=True)
    assert np.array_equal(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax

    # Test with invalid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path="test.png")
    assert np.array_equal(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax

    # Test with invalid data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_coordinates_2d = np.array([[1, 2], [4, 5], [7, 8]])
    expected_ax = plt.subplots()[1]
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path=None)
    assert np.array_equal(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax