import pytest
from src_0444 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func_invalid_tensor_shape():
    P = np.random.rand(5, 3)
    T = np.random.rand(4, 3, 3)
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_valid_input():
    P = np.random.rand(5, 3)
    T = np.random.rand(3, 3, 3)
    cluster_result, ax = task_func(P, T)
    assert isinstance(cluster_result, np.ndarray)
    assert cluster_result.shape == (5, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_parameters():
    P = np.random.rand(5, 3)
    T = np.random.rand(3, 3, 3)
    cluster_result, ax = task_func(P, T, n_clusters=4, random_state=1, n_init=5)
    assert cluster_result.shape == (5, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_cluster_labels():
    P = np.random.rand(5, 3)
    T = np.random.rand(3, 3, 3)
    cluster_result, ax = task_func(P, T)
    unique_labels = np.unique(cluster_result)
    assert len(unique_labels) <= 3  # Since n_clusters is set to 3 by default

def test_task_func_plot():
    P = np.random.rand(5, 3)
    T = np.random.rand(3, 3, 3)
    cluster_result, ax = task_func(P, T)
    assert ax.get_title() == "KMeans Clustering Visualization"
    assert len(ax.collections) > 0  # Check if scatter plot is created