import pytest
from src_0867 import task_func
import numpy as np
from sklearn.cluster import KMeans

def test_task_func():
    # Test case 1: Basic functionality
    data = [(1, 2), (2, 3), (3, 4), (6, 7), (8, 9)]
    expected_labels = np.array([0, 0, 0, 1, 1])
    result = task_func(data)
    assert np.array_equal(result, expected_labels)

    # Add more test cases as needed

# You can add more test cases to cover different scenarios