import pytest
from src_0624 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [[1, 2], [3, 4], [5, 6]]

def test_task_func_output(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_kmeans_labels(sample_data):
    ax = task_func(sample_data)
    data = np.array(list(chain(*sample_data))).reshape(-1, 1)
    kmeans = KMeans(n_clusters=3).fit(data)
    assert np.array_equal(kmeans.labels_, ax.collections[0].get_offsets()[:, 1])

def test_task_func_plot_content(sample_data):
    ax = task_func(sample_data)
    assert len(ax.collections) == 1
    assert len(ax.collections[0].get_offsets()) == len(sample_data) * 2

def test_task_func_plot_colors(sample_data):
    ax = task_func(sample_data)
    colors = ax.collections[0].get_facecolors()
    assert len(colors) == len(sample_data) * 2
    assert all(isinstance(color, tuple) and len(color) == 4 for color in colors)