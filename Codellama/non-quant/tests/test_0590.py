import numpy as np
from src_0590 import task_func


def test_task_func():
    data, kmeans = task_func()
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    assert isinstance(kmeans, KMeans)
    assert kmeans.n_clusters == CLUSTERS
    assert kmeans.cluster_centers_.shape == (CLUSTERS, 2)
    assert kmeans.labels_.shape == (SIZE,)
    assert np.all(kmeans.labels_ >= 0) and np.all(kmeans.labels_ < CLUSTERS)
    assert np.all(kmeans.cluster_centers_ >= 0) and np.all(kmeans.cluster_centers_ < RANGE)