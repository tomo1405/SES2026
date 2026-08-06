python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("'n_clusters' must be an integer greater than 1.")

    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(data)
    centroids = kmeans.cluster_centers_

    fig, ax = plt.subplots()
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=labels, cmap='viridis', alpha=0.6, label='Data points')
    ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='red', label='Centroids')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('K-Means Clustering')
    ax.legend()

    return labels, ax

def test_task_func():
    # Test case 1: Valid input data and n_clusters
    data = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5], 'Feature 2': [6, 7, 8, 9, 10]})
    n_clusters = 2
    labels, ax = task_func(data, n_clusters)
    assert isinstance(labels, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert len(labels) == len(data)
    assert len(set(labels)) == n_clusters
    assert isinstance(ax.collections[0], PathCollection)
    assert ax.collections[0].get_paths()[0].vertices.shape == (5, 2)
    assert ax.collections[1].get_paths()[0].vertices.shape == (2, 2)

    # Test case 2: Invalid input data type
    data = [1, 2, 3, 4, 5]
    n_clusters = 2
    try:
        labels, ax = task_func(data, n_clusters)
    except ValueError as e:
        assert str(e) == "Input 'data' must be a pandas DataFrame."

    # Test case 3: Invalid n_clusters type
    data = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5], 'Feature 2': [6, 7, 8, 9, 10]})
    n_clusters = '2'
    try:
        labels, ax = task_func(data, n_clusters)
    except ValueError as e:
        assert str(e) == "'n_clusters' must be an integer greater than 1."

    # Test case 4: Invalid n_clusters value
    data = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5], 'Feature 2': [6, 7, 8, 9, 10]})
    n_clusters = 1
    try:
        labels, ax = task_func(data, n_clusters)
    except ValueError as e:
        assert str(e) == "'n_clusters' must be an integer greater than 1."