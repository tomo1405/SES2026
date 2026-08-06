python
import numpy as np
from sklearn.cluster import KMeans
import pytest

def task_func(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_
    clusters = {i: np.where(labels == i)[0] for i in range(n_clusters)}
    return clusters

def test_task_func():
    data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    n_clusters = 2
    clusters = task_func(data, n_clusters)
    assert len(clusters) == n_clusters
    assert set(clusters[0]) == set([0, 1, 2])
    assert set(clusters[1]) == set([3, 4, 5])