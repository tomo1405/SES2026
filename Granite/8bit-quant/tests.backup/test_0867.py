import pytest
from src_0867 import task_func

def test_task_func():
    data = [("item1", 1, 2), ("item2", 3, 4), ("item3", 5, 6)]
    n_clusters = 2
    random_state = 0

    expected_labels = [0, 1, 0]

    labels = task_func(data, n_clusters, random_state)

    assert labels == expected_labels