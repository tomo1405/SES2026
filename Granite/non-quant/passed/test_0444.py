import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from src_0444 import task_func

def test_task_func():
    P = np.random.rand(3, 3)
    T = np.random.rand(3, 3, 3)
    n_clusters = 3
    random_state = 0
    n_init = 10
    expected_shape = (3, 3, 3)
    expected_result = np.random.randint(low=0, high=n_clusters, size=(3, 3))
    expected_ax_title = "KMeans Clustering Visualization"

    cluster_result, ax = task_func(P, T, n_clusters, random_state, n_init)

    assert cluster_result.shape == expected_shape
    assert np.array_equal(cluster_result, expected_result)
    assert ax.get_title() == expected_ax_title