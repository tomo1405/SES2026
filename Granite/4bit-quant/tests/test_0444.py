import numpy as np
import pytest
from src_0444 import task_func


def test_task_func():
    P = np.random.rand(3, 3)
    T = np.random.rand(3, 3, 3)
    n_clusters = 3
    random_state = 0
    n_init = 10
    expected_shape = (3, 3, 3)
    expected_result = np.random.randint(low=0, high=n_clusters, size=3)
    expected_ax_title = "KMeans Clustering Visualization"

    cluster_result, ax = task_func(P, T, n_clusters, random_state, n_init)

    assert T.shape == expected_shape, "Provided tensor does not match the expected shape."
    assert np.array_equal(cluster_result, expected_result), "KMeans clustering result is incorrect."
    assert ax.get_title() == expected_ax_title, "Ax title is incorrect."

def test_task_func_value_error():
    P = np.random.rand(3, 3)
    T = np.random.rand(4, 3, 3)
    n_clusters = 3
    random_state = 0
    n_init = 10

    with pytest.raises(ValueError) as e:
        task_func(P, T, n_clusters, random_state, n_init)
    assert str(e.value) == "Provided tensor does not match the expected shape.", "Value error is not raised."