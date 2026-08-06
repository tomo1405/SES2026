import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    # Test with simple data
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6)]
    expected_labels = np.array([0, 0, 0])  # Assuming 1 cluster is formed
    labels = task_func(data, n_clusters=1, random_state=0)
    assert np.array_equal(labels, expected_labels)

    # Test with more clusters
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6), ('item4', 7, 8)]
    expected_labels = np.array([0, 0, 1, 1])  # Assuming 2 clusters are formed
    labels = task_func(data, n_clusters=2, random_state=0)
    assert np.array_equal(labels, expected_labels)

    # Test with different random state
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6)]
    expected_labels = np.array([0, 0, 0])  # Assuming 1 cluster is formed
    labels = task_func(data, n_clusters=1, random_state=1)
    assert np.array_equal(labels, expected_labels)

    # Test with empty data
    data = []
    expected_labels = np.array([])  # No clusters formed
    labels = task_func(data, n_clusters=2, random_state=0)
    assert np.array_equal(labels, expected_labels)

    # Test with single point
    data = [('item1', 1, 2)]
    expected_labels = np.array([0])  # Single cluster formed
    labels = task_func(data, n_clusters=1, random_state=0)
    assert np.array_equal(labels, expected_labels)