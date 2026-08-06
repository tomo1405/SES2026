import numpy as np
from sklearn.cluster import KMeans
from src_0810 import task_func

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    n_clusters = 2
    clusters = task_func(data, n_clusters)
    assert len(clusters) == n_clusters
    for i in range(n_clusters):
        assert len(clusters[i]) > 0

def test_task_func_with_one_cluster():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    n_clusters = 1
    clusters = task_func(data, n_clusters)
    assert len(clusters) == n_clusters
    for i in range(n_clusters):
        assert len(clusters[i]) == len(data)

def test_task_func_with_zero_clusters():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    n_clusters = 0
    clusters = task_func(data, n_clusters)
    assert len(clusters) == 0