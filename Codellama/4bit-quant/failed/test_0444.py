import pytest
from src_0444 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    n_clusters = 3
    random_state = 0
    n_init = 10
    tensor_shape = (3, 3, 3)

    # Test that the function raises an error when the tensor shape is incorrect
    with pytest.raises(ValueError):
        task_func(P, T, n_clusters, random_state, n_init)

    # Test that the function returns the correct result when the tensor shape is correct
    result, ax = task_func(P, T, n_clusters, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (n_clusters, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function returns the correct result when the tensor shape is correct and the number of clusters is 1
    result, ax = task_func(P, T, 1, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function returns the correct result when the tensor shape is correct and the number of clusters is 2
    result, ax = task_func(P, T, 2, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function returns the correct result when the tensor shape is correct and the number of clusters is 3
    result, ax = task_func(P, T, 3, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function returns the correct result when the tensor shape is correct and the number of clusters is 4
    result, ax = task_func(P, T, 4, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (4, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function returns the correct result when the tensor shape is correct and the number of clusters is 5
    result, ax = task_func(P, T, 5, random_state, n_init)
    assert isinstance(result, np.ndarray)
    assert result.shape == (5, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"