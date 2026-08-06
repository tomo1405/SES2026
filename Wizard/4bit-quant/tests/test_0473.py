python
import pytest
from src_0473 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([], 0)

    with pytest.raises(ValueError):
        task_func([1, 2, 3], 0)

    with pytest.raises(ValueError):
        task_func([1, 2, 3], -1)

    myList = [[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]]
    n_clusters = 2
    ax = task_func(myList, n_clusters)
    assert ax.get_xlabel() == "Feature 1"
    assert ax.get_ylabel() == "Feature 2"
    assert len(ax.collections) == 3
    assert len(ax.lines) == 1