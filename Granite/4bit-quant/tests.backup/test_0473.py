import pytest
from src_0473 import task_func

def test_task_func():
    myList = [[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]]
    n_clusters = 2

    with pytest.raises(ValueError):
        task_func([], -1)
        task_func(myList, 0)

    ax = task_func(myList, n_clusters)
    assert ax is not None