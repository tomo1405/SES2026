import pytest
from src_0810 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    n_clusters = 2
    clusters = task_func(data, n_clusters)
    assert len(clusters) == n_clusters
    assert all(len(cluster) > 0 for cluster in clusters.values())
    assert all(cluster.dtype == np.int64 for cluster in clusters.values())
    assert all(cluster.shape[0] == 2 for cluster in clusters.values())
    assert all(cluster.shape[1] == 1 for cluster in clusters.values())