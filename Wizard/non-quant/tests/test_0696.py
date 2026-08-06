python
import numpy as np
import pytest
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    data = np.array(tuples_list)
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return transformed_data

def test_task_func():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 2
    expected_result = np.array([[ 1.41421356, -0.70710678],
                                [ 0.        , -1.41421356],
                                [-1.41421356, -0.70710678]])

    result = task_func(tuples_list, n_components)

    assert np.allclose(result, expected_result)