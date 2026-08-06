import pytest
from src_0810 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    n_clusters = 2
    expected_output = {0: np.array([0, 2]), 1: np.array([1, 3, 4, 5])}
    clusters = task_func(data, n_clusters)
    assert clusters == expected_output

def test_task_func_with_invalid_input():
    data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    n_clusters = 3
    with pytest.raises(ValueError):
        task_func(data, n_clusters)