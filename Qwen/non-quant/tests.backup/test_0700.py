import pytest
from src_0700 import task_func
import pandas as pd
from sklearn.cluster import KMeans

def test_task_func():
    # Test with default parameters
    x_list = [1, 2, 3, 4, 5]
    y_list = [5, 4, 3, 2, 1]
    labels, centers = task_func(x_list, y_list)
    assert isinstance(labels, list)
    assert len(labels) == len(x_list)
    assert isinstance(centers, list)
    assert len(centers) == 2
    assert all(isinstance(center, list) and len(center) == 2 for center in centers)

    # Test with different number of clusters
    labels, centers = task_func(x_list, y_list, n_clusters=3)
    assert len(centers) == 3

    # Test with different random state
    labels1, _ = task_func(x_list, y_list, random_state=1)
    labels2, _ = task_func(x_list, y_list, random_state=1)
    assert labels1 == labels2

    # Test with empty lists
    labels, centers = task_func([], [])
    assert labels == []
    assert centers == []

    # Test with single element lists
    labels, centers = task_func([1], [1])
    assert labels == [0]
    assert len(centers) == 1
    assert len(centers[0]) == 2

    # Test with negative values
    labels, centers = task_func([-1, -2, -3], [-3, -2, -1])
    assert isinstance(labels, list)
    assert len(labels) == 3
    assert isinstance(centers, list)
    assert len(centers) == 2
    assert all(isinstance(center, list) and len(center) == 2 for center in centers)