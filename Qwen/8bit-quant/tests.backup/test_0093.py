import pytest
from src_0093 import task_func
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def test_task_func_input_data_type():
    with pytest.raises(ValueError, match="Input 'data' must be a pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_n_clusters_type():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    with pytest.raises(ValueError, match="'n_clusters' must be an integer greater than 1."):
        task_func(data, n_clusters=1)

def test_task_func_n_clusters_value():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    with pytest.raises(ValueError, match="'n_clusters' must be an integer greater than 1."):
        task_func(data, n_clusters=0)

def test_task_func_output_types():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    labels, ax = task_func(data)
    assert isinstance(labels, np.ndarray)
    assert isinstance(ax, Axes)

def test_task_func_output_labels_length():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    labels, _ = task_func(data)
    assert len(labels) == len(data)

def test_task_func_kmeans_clustering():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    labels, _ = task_func(data, n_clusters=2)
    assert len(np.unique(labels)) == 2

def test_task_func_plotting():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    _, ax = task_func(data)
    assert isinstance(ax.collections[0], PathCollection)  # Data points
    assert isinstance(ax.collections[1], PathCollection)  # Centroids