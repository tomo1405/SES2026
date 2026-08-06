import pytest
from src_0700 import task_func

def test_task_func():
    x_list = [1, 2, 3, 4, 5]
    y_list = [1, 2, 3, 4, 5]
    n_clusters = 2
    random_state = 0
    expected_labels = [0, 0, 1, 1, 0]
    expected_centers = [[2, 2], [4, 4]]

    labels, centers = task_func(x_list, y_list, n_clusters, random_state)

    assert labels == expected_labels
    assert centers == expected_centers