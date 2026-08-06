import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    n_clusters = 2
    random_state = 0

    labels = task_func(data, n_clusters, random_state)

    assert len(labels) == len(data)
    assert np.all(labels >= 0)
    assert np.all(labels < n_clusters)

def test_task_func_with_invalid_data():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    n_clusters = 2
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, n_clusters, random_state, invalid_param=True)

def test_task_func_with_invalid_n_clusters():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    n_clusters = 0
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, n_clusters, random_state)

def test_task_func_with_invalid_random_state():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    n_clusters = 2
    random_state = -1

    with pytest.raises(ValueError):
        task_func(data, n_clusters, random_state)