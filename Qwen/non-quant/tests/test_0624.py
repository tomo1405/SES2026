import matplotlib.pyplot as plt
import numpy as np
import pytest
from sklearn.cluster import KMeans
from src_0624 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list of lists")

def test_task_func_input_content():
    with pytest.raises(ValueError):
        task_func([[1, 2], "not a list"])

def test_task_func_output_type():
    ax = task_func([[1, 2], [3, 4]])
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_fit():
    data = [[1, 2], [3, 4]]
    ax = task_func(data)
    flat_data = np.array(list(chain(*data))).reshape(-1, 1)
    kmeans = KMeans(n_clusters=3).fit(flat_data)
    assert np.array_equal(kmeans.labels_, ax.collections[0].get_array().astype(int))

def test_task_func_scatter_plot():
    data = [[1, 2], [3, 4]]
    ax = task_func(data)
    assert len(ax.collections) == 1
    assert ax.collections[0].get_offsets().shape == (4, 2)
    assert np.allclose(ax.collections[0].get_offsets()[:, 1], 0)

def test_task_func_cluster_labels():
    data = [[1, 2], [3, 4]]
    ax = task_func(data)
    labels = ax.collections[0].get_array().astype(int)
    assert np.unique(labels).size <= 3