import pytest
from src_0810 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    # Test case 1: Basic test
    data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 2]])
    n_clusters = 2
    expected_clusters = {0: np.array([0, 2]), 1: np.array([1, 3, 4, 5])}
    result = task_func(data, n_clusters)
    assert result == expected_clusters

    # Add more test cases as needed

# Note: The above test case is a basic example. You can add more test cases to cover different scenarios.