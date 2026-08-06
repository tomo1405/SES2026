import pytest
from src_0696 import task_func
import numpy as np
from sklearn.decomposition import PCA

def test_task_func():
    # Test case 1: Basic test with a simple list of tuples
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 1
    result = task_func(tuples_list, n_components)
    expected_result = np.array([[1, 2], [3, 4], [5, 6]])
    assert np.allclose(result, expected_result)

    # Add more test cases as needed

    # Add more test cases to cover different scenarios