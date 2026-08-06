import pytest
from src_0444 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func_input_shape():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 3, 3)
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_kmeans_result():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 3, 3).reshape((3, 3, 3))
    cluster_result, _ = task_func(P, T, n_clusters=2)
    assert isinstance(cluster_result, np.ndarray)
    assert len(np.unique(cluster_result)) <= 2

def test_task_func_plot_return_type():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 3, 3).reshape((3, 3, 3))
    _, ax = task_func(P, T)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_state_consistency():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 3, 3).reshape((3, 3, 3))
    cluster_result_1, _ = task_func(P, T, random_state=42)
    cluster_result_2, _ = task_func(P, T, random_state=42)
    assert np.array_equal(cluster_result_1, cluster_result_2)

def test_task_func_n_init_effect():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 3, 3).reshape((3, 3, 3))
    cluster_result_1, _ = task_func(P, T, n_init=1)
    cluster_result_2, _ = task_func(P, T, n_init=10)
    assert not np.array_equal(cluster_result_1, cluster_result_2)