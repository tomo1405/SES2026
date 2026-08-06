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
    cluster_result, ax = task_func(P, T, n_clusters, random_state, n_init)
    assert isinstance(cluster_result, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert cluster_result.shape == (P.shape[0],)
    assert ax.get_title() == "KMeans Clustering Visualization"

def test_task_func_value_error():
    P = np.random.rand(3, 3)
    T = np.random.rand(3, 3, 2)
    n_clusters = 3
    random_state = 0
    n_init = 10
    try:
        task_func(P, T, n_clusters, random_state, n_init)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError was not raised"