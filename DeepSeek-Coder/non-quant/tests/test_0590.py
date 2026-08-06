import pytest
from src_0590 import task_func

def test_task_func():
    data, kmeans = task_func()
    assert isinstance(data, np.ndarray), "The data should be a numpy array"
    assert isinstance(kmeans, type(KMeans(n_clusters=5)), "The kmeans object should be of type KMeans"
    assert len(data) == 1000, "The data should contain 1000 points"
    assert len(kmeans.cluster_centers_) == 5, "The number of clusters should be 5"