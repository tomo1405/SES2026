import pytest
from src_0810 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func_with_two_clusters():
    data = np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0]])
    n_clusters = 2
    result = task_func(data, n_clusters)
    assert len(result) == n_clusters
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == len(data)

def test_task_func_with_single_cluster():
    data = np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0]])
    n_clusters = 1
    result = task_func(data, n_clusters)
    assert len(result) == n_clusters
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == len(data)

def test_task_func_with_more_clusters_than_data_points():
    data = np.array([[1, 2]])
    n_clusters = 3
    result = task_func(data, n_clusters)
    assert len(result) == n_clusters
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == len(data)

def test_task_func_with_empty_data():
    data = np.array([])
    n_clusters = 2
    result = task_func(data, n_clusters)
    assert len(result) == n_clusters
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == len(data)

def test_task_func_with_one_data_point():
    data = np.array([[1, 2]])
    n_clusters = 1
    result = task_func(data, n_clusters)
    assert len(result) == n_clusters
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == len(data)