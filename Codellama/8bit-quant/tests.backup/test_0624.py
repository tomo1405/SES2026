import pytest
from src_0624 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert ax.get_xlabel() == 'data'
    assert ax.get_ylabel() == '0'
    assert ax.get_title() == 'KMeans Clustering'
    assert len(ax.get_legend_handles_labels()[0]) == 3
    assert len(ax.get_legend_handles_labels()[1]) == 3
    assert ax.get_legend_handles_labels()[0][0].get_text() == 'Cluster 0'
    assert ax.get_legend_handles_labels()[0][1].get_text() == 'Cluster 1'
    assert ax.get_legend_handles_labels()[0][2].get_text() == 'Cluster 2'
    assert ax.get_legend_handles_labels()[1][0].get_text() == 'Cluster 0'
    assert ax.get_legend_handles_labels()[1][1].get_text() == 'Cluster 1'
    assert ax.get_legend_handles_labels()[1][2].get_text() == 'Cluster 2'