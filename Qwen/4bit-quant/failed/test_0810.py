import pytest
from src_0810 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [1, 4], [1, 0],
                     [4, 2], [4, 4], [4, 0]])

def test_task_func_with_valid_input(sample_data):
    result = task_func(sample_data, 2)
    assert len(result) == 2
    assert all(isinstance(cluster, np.ndarray) for cluster in result.values())
    assert np.sum([len(cluster) for cluster in result.values()]) == sample_data.shape[0]

def test_task_func_with_one_cluster(sample_data):
    result = task_func(sample_data, 1)
    assert len(result) == 1
    assert len(result[0]) == sample_data.shape[0]

def test_task_func_with_more_clusters_than_samples(sample_data):
    result = task_func(sample_data, 10)
    assert len(result) == 10
    assert sum(len(cluster) for cluster in result.values()) == sample_data.shape[0]

def test_task_func_with_zero_clusters(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, 0)

def test_task_func_with_negative_clusters(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, -1)

def test_task_func_with_non_numeric_data():
    with pytest.raises(TypeError):
        task_func(np.array([[1, 'a'], [1, 4], [1, 0]]), 2)

def test_task_func_with_empty_data():
    result = task_func(np.empty((0, 2)), 3)
    assert len(result) == 3
    assert all(len(cluster) == 0 for cluster in result.values())