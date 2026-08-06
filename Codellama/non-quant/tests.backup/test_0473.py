import pytest
from src_0473 import task_func

def test_task_func():
    myList = [(1, 2), (3, 4), (5, 6), (7, 8)]
    n_clusters = 2
    ax = task_func(myList, n_clusters)
    assert ax.has_data()
    assert len(ax.collections) == 2
    assert ax.collections[0].get_label() == "Cluster 0"
    assert ax.collections[1].get_label() == "Cluster 1"
    assert ax.collections[0].get_color() == "red"
    assert ax.collections[1].get_color() == "red"
    assert ax.collections[0].get_marker() == "o"
    assert ax.collections[1].get_marker() == "o"
    assert ax.collections[0].get_sizes() == [10]
    assert ax.collections[1].get_sizes() == [10]
    assert ax.collections[0].get_offsets() == [(1, 2), (3, 4)]
    assert ax.collections[1].get_offsets() == [(5, 6), (7, 8)]