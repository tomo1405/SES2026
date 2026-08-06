import numpy as np
from src_0590 import task_func


def test_task_func():
    data, kmeans = task_func()
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    assert isinstance(kmeans, KMeans)
    assert kmeans.n_clusters == CLUSTERS
    assert kmeans.cluster_centers_.shape == (CLUSTERS, 2)