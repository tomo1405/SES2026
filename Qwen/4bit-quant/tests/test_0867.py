import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func_with_default_parameters():
    data = [
        (1, 1.0, 2.0),
        (2, 1.5, 1.8),
        (3, 5.0, 8.0),
        (4, 8.0, 8.0),
        (5, 1.0, 0.6),
        (6, 9.0, 11.0)
    ]
    expected_labels = [0, 0, 1, 1, 0, 1]
    labels = task_func(data)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_custom_n_clusters():
    data = [
        (1, 1.0, 2.0),
        (2, 1.5, 1.8),
        (3, 5.0, 8.0),
        (4, 8.0, 8.0),
        (5, 1.0, 0.6),
        (6, 9.0, 11.0)
    ]
    expected_labels = [0, 0, 1, 1, 0, 1]  # Assuming 2 clusters is optimal for this dataset
    labels = task_func(data, n_clusters=2)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_random_state():
    data = [
        (1, 1.0, 2.0),
        (2, 1.5, 1.8),
        (3, 5.0, 8.0),
        (4, 8.0, 8.0),
        (5, 1.0, 0.6),
        (6, 9.0, 11.0)
    ]
    expected_labels = [0, 0, 1, 1, 0, 1]
    labels = task_func(data, random_state=0)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_single_point():
    data = [(1, 1.0, 2.0)]
    expected_labels = [0]
    labels = task_func(data)
    assert np.array_equal(labels, expected_labels)

def test_task_func_with_empty_data():
    data = []
    expected_labels = []
    labels = task_func(data)
    assert np.array_equal(labels, expected_labels)