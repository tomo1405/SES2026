import pytest
from src_0444 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func_input_shape():
    P = np.random.rand(4, 3)
    T = np.random.rand(3, 3, 3)
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_output_shape():
    P = np.random.rand(5, 3)
    T = np.ones((3, 3, 3))
    cluster_result, ax = task_func(P, T)
    assert cluster_result.shape == (5,)
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_fit():
    P = np.random.rand(5, 3)
    T = np.ones((3, 3, 3))
    cluster_result, ax = task_func(P, T)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
    flattened_result = np.tensordot(P, T, axes=[1, 1]).swapaxes(0, 1).reshape(-1, 3)
    assert np.array_equal(cluster_result, kmeans.fit_predict(flattened_result))

def test_task_func_plot():
    P = np.random.rand(5, 3)
    T = np.ones((3, 3, 3))
    _, ax = task_func(P, T)
    assert len(ax.collections) == 1  # There should be one scatter plot collection
    assert ax.get_title() == "KMeans Clustering Visualization"