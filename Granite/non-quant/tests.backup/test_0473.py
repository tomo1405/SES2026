import pytest
from src_0473 import task_func

def test_task_func():
    myList = [[1, 2], [3, 4], [5, 6], [7, 8]]
    n_clusters = 2

    with pytest.raises(ValueError):
        task_func([], n_clusters)
    with pytest.raises(ValueError):
        task_func(myList, 0)

    ax = task_func(myList, n_clusters)
    assert ax is not None