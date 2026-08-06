import pytest
from src_0700 import task_func

def test_task_func():
    x_list = [1, 2, 3, 4, 5]
    y_list = [1, 2, 3, 4, 5]
    n_clusters = 2
    random_state = 0
    labels, centers = task_func(x_list, y_list, n_clusters, random_state)
    assert len(labels) == len(x_list)
    assert len(centers) == n_clusters
    assert all(label in range(n_clusters) for label in labels)
    assert all(center in range(n_clusters) for center in centers)