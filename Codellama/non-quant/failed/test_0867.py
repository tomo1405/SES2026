import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    n_clusters = 2
    random_state = 0

    labels = task_func(data, n_clusters, random_state)

    assert len(labels) == len(data)
    assert all(isinstance(label, int) for label in labels)
    assert all(label >= 0 for label in labels)
    assert all(label < n_clusters for label in labels)

    # Test with different number of clusters
    n_clusters = 3
    labels = task_func(data, n_clusters, random_state)
    assert len(labels) == len(data)
    assert all(isinstance(label, int) for label in labels)
    assert all(label >= 0 for label in labels)
    assert all(label < n_clusters for label in labels)

    # Test with different random state
    random_state = 1
    labels = task_func(data, n_clusters, random_state)
    assert len(labels) == len(data)
    assert all(isinstance(label, int) for label in labels)
    assert all(label >= 0 for label in labels)
    assert all(label < n_clusters for label in labels)

    # Test with different data
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    labels = task_func(data, n_clusters, random_state)
    assert len(labels) == len(data)
    assert all(isinstance(label, int) for label in labels)
    assert all(label >= 0 for label in labels)
    assert all(label < n_clusters for label in labels)