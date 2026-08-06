import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func_with_default_parameters():
    data = [
        ('item1', 1.0, 2.0),
        ('item2', 3.0, 4.0),
        ('item3', 5.0, 6.0),
        ('item4', 7.0, 8.0)
    ]
    expected_labels = np.array([0, 0, 1, 1])  # This is an example, actual labels may vary
    labels = task_func(data)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_custom_n_clusters():
    data = [
        ('item1', 1.0, 2.0),
        ('item2', 3.0, 4.0),
        ('item3', 5.0, 6.0),
        ('item4', 7.0, 8.0)
    ]
    expected_labels = np.array([0, 1, 0, 1])  # This is an example, actual labels may vary
    labels = task_func(data, n_clusters=2)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_custom_random_state():
    data = [
        ('item1', 1.0, 2.0),
        ('item2', 3.0, 4.0),
        ('item3', 5.0, 6.0),
        ('item4', 7.0, 8.0)
    ]
    expected_labels = np.array([0, 0, 1, 1])  # This is an example, actual labels may vary
    labels = task_func(data, random_state=42)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_single_cluster():
    data = [
        ('item1', 1.0, 2.0),
        ('item2', 3.0, 4.0),
        ('item3', 5.0, 6.0),
        ('item4', 7.0, 8.0)
    ]
    expected_labels = np.array([0, 0, 0, 0])  # All items in one cluster
    labels = task_func(data, n_clusters=1)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_no_data():
    data = []
    expected_labels = np.array([])  # No labels for no data
    labels = task_func(data)
    assert np.array_equal(labels, expected_labels)