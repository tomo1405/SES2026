import pytest
from src_0473 import task_func

def test_task_func():
    myList = [(1, 2), (3, 4), (5, 6)]
    n_clusters = 2
    ax = task_func(myList, n_clusters)
    assert ax.has_data()
    assert len(ax.get_lines()) == 2
    assert len(ax.get_patches()) == 2
    assert len(ax.get_collections()) == 2
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_title() == "Clustering"

def test_task_func_invalid_input():
    myList = []
    n_clusters = 0
    with pytest.raises(ValueError):
        task_func(myList, n_clusters)