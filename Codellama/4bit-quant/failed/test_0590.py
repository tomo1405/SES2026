import pytest
from src_0590 import task_func

def test_task_func():
    data, kmeans = task_func()
    assert isinstance(data, np.ndarray)
    assert data.shape == (SIZE, 2)
    assert isinstance(kmeans, KMeans)
    assert kmeans.n_clusters == CLUSTERS
    assert kmeans.cluster_centers_.shape == (CLUSTERS, 2)
    assert kmeans.labels_.shape == (SIZE,)
    assert np.all(kmeans.labels_ >= 0)
    assert np.all(kmeans.labels_ < CLUSTERS)
    assert np.all(kmeans.cluster_centers_ >= 0)
    assert np.all(kmeans.cluster_centers_ < RANGE)
    assert np.all(data[:, 0] >= 0)
    assert np.all(data[:, 0] < RANGE)
    assert np.all(data[:, 1] >= 0)
    assert np.all(data[:, 1] < RANGE)
    assert np.all(kmeans.labels_ == np.argmin(np.linalg.norm(data - kmeans.cluster_centers_, axis=1), axis=1))