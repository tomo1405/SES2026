import pytest
from src_0700 import task_func
import pandas as pd
from sklearn.cluster import KMeans

def test_task_func():
    # Test with simple data
    x_list = [1, 2, 3, 4, 5]
    y_list = [1, 2, 3, 4, 5]
    labels, centers = task_func(x_list, y_list, n_clusters=2, random_state=0)
    
    assert isinstance(labels, list)
    assert isinstance(centers, np.ndarray)
    assert len(labels) == len(x_list)
    assert centers.shape == (2, 2)

    # Test with different number of clusters
    labels, centers = task_func(x_list, y_list, n_clusters=3, random_state=0)
    assert centers.shape == (3, 2)

    # Test with empty lists
    labels, centers = task_func([], [], n_clusters=1, random_state=0)
    assert labels == []
    assert centers.shape == (1, 2)

    # Test with one element
    labels, centers = task_func([1], [1], n_clusters=1, random_state=0)
    assert labels == [0]
    assert centers.shape == (1, 2)

    # Test with different random state
    labels1, centers1 = task_func(x_list, y_list, n_clusters=2, random_state=0)
    labels2, centers2 = task_func(x_list, y_list, n_clusters=2, random_state=1)
    assert not np.array_equal(labels1, labels2)
    assert not np.array_equal(centers1, centers2)