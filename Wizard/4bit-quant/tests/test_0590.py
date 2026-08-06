python
import pytest
from src_0590 import task_func

def test_task_func():
    data, kmeans = task_func()
    assert data.shape == (1000, 2)
    assert kmeans.labels_.shape == (1000,)
    assert kmeans.cluster_centers_.shape == (5, 2)