python
import numpy as np
import pytest
from src_0810 import task_func

def test_task_func():
    data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    n_clusters = 2
    clusters = task_func(data, n_clusters)
    assert len(clusters) == n_clusters
    for i in range(n_clusters):
        assert len(clusters[i]) > 0