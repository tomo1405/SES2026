import pytest
from src_0444 import task_func
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
    n_clusters = 3
    random_state = 0
    n_init = 10

    result, ax = task_func(P, T, n_clusters, random_state, n_init)

    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "KMeans Clustering Visualization"

    # Test that the function raises an error when the tensor shape is incorrect
    with pytest.raises(ValueError):
        task_func(P, T, n_clusters, random_state, n_init, tensor_shape=(4, 4, 4))