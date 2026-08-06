import pytest
from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
def task_func(L):
    N_CLUSTERS = 3
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)
    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(data)
    fig, ax = plt.subplots()
    ax.scatter(data, [0]*len(data), c=kmeans.labels_.astype(float))
    return ax
def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert ax is not None
def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func([[1, 2], [3, 4], [5]])