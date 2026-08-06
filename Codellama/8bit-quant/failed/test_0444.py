import pytest
from src_0444 import task_func
import numpy as np

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
    n_clusters = 3
    random_state = 0
    n_init = 10

    result, ax = task_func(P, T, n_clusters, random_state, n_init)

    assert result.shape == (3, 3, 3)
    assert ax.get_title() == "KMeans Clustering Visualization"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_zlabel() == "z"