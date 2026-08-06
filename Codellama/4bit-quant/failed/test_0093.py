import pytest
from src_0093 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def test_task_func():
    # Test 1: Input data is not a pandas DataFrame
    data = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        task_func(data)

    # Test 2: Number of clusters is not an integer greater than 1
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    with pytest.raises(ValueError):
        task_func(data, n_clusters=0)

    # Test 3: Input data is a pandas DataFrame
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data)
    assert isinstance(labels, pd.Series)
    assert isinstance(ax, plt.Axes)

    # Test 4: Number of clusters is an integer greater than 1
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data, n_clusters=3)
    assert isinstance(labels, pd.Series)
    assert isinstance(ax, plt.Axes)

    # Test 5: Centroids are plotted correctly
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data, n_clusters=3)
    assert len(ax.collections) == 2
    assert isinstance(ax.collections[0], PathCollection)
    assert isinstance(ax.collections[1], PathCollection)
    assert ax.collections[0].get_offsets().shape == (3, 2)
    assert ax.collections[1].get_offsets().shape == (3, 2)

    # Test 6: Data points are plotted correctly
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data, n_clusters=3)
    assert len(ax.collections) == 2
    assert isinstance(ax.collections[0], PathCollection)
    assert isinstance(ax.collections[1], PathCollection)
    assert ax.collections[0].get_offsets().shape == (5, 2)
    assert ax.collections[1].get_offsets().shape == (3, 2)

    # Test 7: Labels are returned correctly
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data, n_clusters=3)
    assert len(labels) == 5
    assert isinstance(labels, pd.Series)
    assert labels.dtype == np.int64

    # Test 8: Axes are returned correctly
    data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    labels, ax = task_func(data, n_clusters=3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Feature 1'
    assert ax.get_ylabel() == 'Feature 2'
    assert ax.get_title() == 'K-Means Clustering'