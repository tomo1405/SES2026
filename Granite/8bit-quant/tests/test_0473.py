import pytest
from src_0473 import task_func

def test_task_func_valid_inputs():
    myList = [[1, 2], [3, 4], [5, 6]]
    n_clusters = 2
    ax = task_func(myList, n_clusters)
    assert ax is not None

def test_task_func_invalid_inputs():
    myList = []
    n_clusters = 0
    with pytest.raises(ValueError):
        task_func(myList, n_clusters)

def test_task_func_n_clusters_lt_1():
    myList = [[1, 2], [3, 4], [5, 6]]
    n_clusters = -1
    with pytest.raises(ValueError):
        task_func(myList, n_clusters)