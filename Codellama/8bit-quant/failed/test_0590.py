import pytest
from src_0590 import task_func

def test_task_func():
    data, kmeans = task_func()
    assert len(data) == SIZE
    assert len(kmeans.labels_) == SIZE
    assert len(kmeans.cluster_centers_) == CLUSTERS
    assert np.all(kmeans.labels_ >= 0)
    assert np.all(kmeans.labels_ < CLUSTERS)
    assert np.all(kmeans.cluster_centers_ >= 0)
    assert np.all(kmeans.cluster_centers_ < RANGE)